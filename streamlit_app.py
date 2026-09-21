import streamlit as st
from db_connection import get_connection
from datetime import date


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="Green Bloom",
    page_icon="🌱",
    layout="wide"
)


# =========================================================
# SIDEBAR MENU
# =========================================================

st.sidebar.title("🌿 Green Bloom")
st.sidebar.write("Plant Stock Management System")

menu = st.sidebar.selectbox(
    "Select Menu",
    [
        "🏠 Home",
        "🌱 Plants",
        "➕ Add Plant",
        "✏️ Update Quantity",
        "🗑️ Delete Plant",
        "🚚 Suppliers",
        "👤 Customers",
        "🧾 Billing",
        "📊 Sales Report"
    ]
)


# =========================================================
# HOME
# =========================================================

if menu == "🏠 Home":

    st.title("🌿 Green Bloom Plants")
    st.subheader("Plant Stock Management System")

    st.write(
        "Welcome to Green Bloom Plant Nursery. "
        "Manage plants, suppliers, customers, billing and sales easily."
    )

    st.markdown("## 🌳 Our Green World")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image(
            "images/rose.jpg",
            caption="🌹 Rose",
            use_container_width=True
        )

    with col2:
        st.image(
            "images/jasmine.jpg",
            caption="🌼 Jasmine",
            use_container_width=True
        )

    with col3:
        st.image(
            "images/aloe_vera.jpg",
            caption="🌿 Aloe Vera",
            use_container_width=True
        )

    with col4:
        st.image(
            "images/money_plant.jpg",
            caption="🌱 Money Plant",
            use_container_width=True
        )

    st.markdown("## 🌱 About Green Bloom")

    st.info(
        "Green Bloom is a Plant Stock Management System "
        "used to manage plant stock, suppliers, customers, "
        "billing and sales records."
    )


# =========================================================
# PLANTS
# =========================================================

elif menu == "🌱 Plants":

    st.title("🌱 Plant Stock")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            plant_id,
            plant_name,
            category,
            price,
            quantity,
            supplier_name
        FROM plants
        ORDER BY plant_id
    """)

    plants = cursor.fetchall()

    cursor.close()
    connection.close()

    if len(plants) == 0:

        st.info("No plants available.")

    else:

        for plant in plants:

            st.markdown(f"### 🌿 {plant[1]}")

            col1, col2, col3, col4, col5, col6 = st.columns(6)

            with col1:
                st.write("**Plant ID**")
                st.write(plant[0])

            with col2:
                st.write("**Plant Name**")
                st.write(plant[1])

            with col3:
                st.write("**Category**")
                st.write(plant[2])

            with col4:
                st.write("**Price**")
                st.write(f"₹{plant[3]}")

            with col5:
                st.write("**Quantity**")
                st.write(plant[4])

            with col6:
                st.write("**Supplier**")
                st.write(plant[5])

            st.divider()


# =========================================================
# ADD PLANT
# =========================================================

elif menu == "➕ Add Plant":

    st.title("➕ Add New Plant")

    plant_id = st.number_input(
        "Plant ID",
        min_value=1,
        step=1
    )

    plant_name = st.text_input("Plant Name")

    category = st.text_input("Category")

    price = st.number_input(
        "Price",
        min_value=0.0,
        step=1.0
    )

    quantity = st.number_input(
        "Quantity",
        min_value=0,
        step=1
    )

    supplier_name = st.text_input("Supplier Name")

    if st.button("Add Plant"):

        if (
            plant_name.strip() == ""
            or category.strip() == ""
            or supplier_name.strip() == ""
        ):

            st.warning("Please fill all fields.")

        else:

            connection = get_connection()
            cursor = connection.cursor()

            try:

                cursor.execute(
                    """
                    INSERT INTO plants
                    (
                        plant_id,
                        plant_name,
                        category,
                        price,
                        quantity,
                        supplier_name
                    )
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """,
                    (
                        plant_id,
                        plant_name,
                        category,
                        price,
                        quantity,
                        supplier_name
                    )
                )

                connection.commit()

                st.success("Plant added successfully.")

            except Exception as e:

                connection.rollback()
                st.error(f"Error: {e}")

            finally:

                cursor.close()
                connection.close()


# =========================================================
# UPDATE QUANTITY
# =========================================================

elif menu == "✏️ Update Quantity":

    st.title("✏️ Update Plant Quantity")

    plant_id = st.number_input(
        "Plant ID",
        min_value=1,
        step=1
    )

    new_quantity = st.number_input(
        "New Quantity",
        min_value=0,
        step=1
    )

    if st.button("Update Quantity"):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                UPDATE plants
                SET quantity = %s
                WHERE plant_id = %s
                """,
                (
                    new_quantity,
                    plant_id
                )
            )

            connection.commit()

            if cursor.rowcount > 0:

                st.success(
                    "Plant quantity updated successfully."
                )

            else:

                st.warning("Plant not found.")

        except Exception as e:

            connection.rollback()
            st.error(f"Error: {e}")

        finally:

            cursor.close()
            connection.close()


# =========================================================
# DELETE PLANT
# =========================================================

elif menu == "🗑️ Delete Plant":

    st.title("🗑️ Delete Plant")

    plant_id = st.number_input(
        "Plant ID to Delete",
        min_value=1,
        step=1
    )

    if st.button("Delete Plant"):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                DELETE FROM plants
                WHERE plant_id = %s
                """,
                (plant_id,)
            )

            connection.commit()

            if cursor.rowcount > 0:

                st.success("Plant deleted successfully.")

            else:

                st.warning("Plant not found.")

        except Exception as e:

            connection.rollback()
            st.error(f"Error: {e}")

        finally:

            cursor.close()
            connection.close()


# =========================================================
# SUPPLIERS
# =========================================================

elif menu == "🚚 Suppliers":

    st.title("🚚 Suppliers")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            supplier_id,
            supplier_name,
            phone,
            city
        FROM suppliers
        ORDER BY supplier_id
    """)

    suppliers = cursor.fetchall()

    cursor.close()
    connection.close()

    if len(suppliers) == 0:

        st.info("No suppliers available.")

    else:

        for supplier in suppliers:

            st.markdown(f"### 🚚 {supplier[1]}")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.write("**Supplier ID**")
                st.write(supplier[0])

            with col2:
                st.write("**Supplier Name**")
                st.write(supplier[1])

            with col3:
                st.write("**Phone**")
                st.write(supplier[2])

            with col4:
                st.write("**City**")
                st.write(supplier[3])

            st.divider()


# =========================================================
# CUSTOMERS
# =========================================================

elif menu == "👤 Customers":

    st.title("👤 Customers")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            customer_id,
            customer_name,
            phone,
            city
        FROM customers
        ORDER BY customer_id
    """)

    customers = cursor.fetchall()

    cursor.close()
    connection.close()

    if len(customers) == 0:

        st.info("No customers available.")

    else:

        for customer in customers:

            st.markdown(f"### 👤 {customer[1]}")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.write("**Customer ID**")
                st.write(customer[0])

            with col2:
                st.write("**Customer Name**")
                st.write(customer[1])

            with col3:
                st.write("**Phone**")
                st.write(customer[2])

            with col4:
                st.write("**City**")
                st.write(customer[3])

            st.divider()


# =========================================================
# BILLING
# =========================================================

elif menu == "🧾 Billing":

    st.title("🧾 Green Bloom Billing")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            plant_name,
            price,
            quantity
        FROM plants
        WHERE quantity > 0
        ORDER BY plant_name
    """)

    plants = cursor.fetchall()

    cursor.close()
    connection.close()

    if len(plants) == 0:

        st.warning("No plants available for sale.")

    else:

        customer_name = st.text_input(
            "Customer Name"
        )

        plant_names = []

        for plant in plants:
            plant_names.append(plant[0])

        selected_plant = st.selectbox(
            "Select Plant",
            plant_names
        )

        selected_data = None

        for plant in plants:

            if plant[0] == selected_plant:

                selected_data = plant
                break

        price = selected_data[1]
        available_quantity = selected_data[2]

        st.write("**Price:**", f"₹{price}")
        st.write(
            "**Available Quantity:**",
            available_quantity
        )

        sale_quantity = st.number_input(
            "Quantity",
            min_value=1,
            max_value=available_quantity,
            step=1
        )

        total_amount = price * sale_quantity

        st.markdown("### 💰 Total Amount")

        st.write(f"## ₹{total_amount:.2f}")

        if st.button("Generate Bill"):

            if customer_name.strip() == "":

                st.warning(
                    "Please enter customer name."
                )

            else:

                connection = get_connection()
                cursor = connection.cursor()

                try:

                    # Insert sale record
                    cursor.execute(
                        """
                        INSERT INTO sales
                        (
                            customer_name,
                            plant_name,
                            quantity,
                            total_amount,
                            sale_date
                        )
                        VALUES (%s, %s, %s, %s, %s)
                        """,
                        (
                            customer_name,
                            selected_plant,
                            sale_quantity,
                            total_amount,
                            date.today()
                        )
                    )

                    # Reduce plant quantity
                    cursor.execute(
                        """
                        UPDATE plants
                        SET quantity = quantity - %s
                        WHERE plant_name = %s
                        AND quantity >= %s
                        """,
                        (
                            sale_quantity,
                            selected_plant,
                            sale_quantity
                        )
                    )

                    if cursor.rowcount == 0:

                        connection.rollback()

                        st.error(
                            "Insufficient stock."
                        )

                    else:

                        connection.commit()

                        st.success(
                            "Bill generated successfully."
                        )

                        st.markdown("---")

                        st.markdown(
                            "## 🧾 Green Bloom Bill"
                        )

                        st.write(
                            "**Customer Name:**",
                            customer_name
                        )

                        st.write(
                            "**Plant Name:**",
                            selected_plant
                        )

                        st.write(
                            "**Quantity:**",
                            sale_quantity
                        )

                        st.write(
                            "**Price:**",
                            f"₹{price:.2f}"
                        )

                        st.write(
                            "**Total Amount:**",
                            f"₹{total_amount:.2f}"
                        )

                        st.write(
                            "**Date:**",
                            date.today()
                        )

                        st.markdown("---")

                        st.success(
                            "Thank you for shopping with Green Bloom! 🌱"
                        )

                except Exception as e:

                    connection.rollback()
                    st.error(f"Error: {e}")

                finally:

                    cursor.close()
                    connection.close()


# =========================================================
# SALES REPORT
# =========================================================

elif menu == "📊 Sales Report":

    st.title("📊 Sales Report")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            sale_id,
            customer_name,
            plant_name,
            quantity,
            total_amount,
            sale_date
        FROM sales
        ORDER BY sale_id DESC
    """)

    sales = cursor.fetchall()

    cursor.close()
    connection.close()

    if len(sales) == 0:

        st.info("No sales available.")

    else:

        for sale in sales:

            st.markdown(f"### 🧾 Sale #{sale[0]}")

            col1, col2, col3, col4, col5, col6 = st.columns(6)

            with col1:
                st.write("**Sale ID**")
                st.write(sale[0])

            with col2:
                st.write("**Customer**")
                st.write(sale[1])

            with col3:
                st.write("**Plant**")
                st.write(sale[2])

            with col4:
                st.write("**Quantity**")
                st.write(sale[3])

            with col5:
                st.write("**Total Amount**")
                st.write(f"₹{sale[4]:.2f}")

            with col6:
                st.write("**Sale Date**")
                st.write(sale[5])

            st.divider()
