import streamlit as st
from db_connection import get_connection
from datetime import date


st.set_page_config(
    page_title="Green Bloom",
    page_icon="🌱",
    layout="wide"
)


# =========================================================
# PLANT IMAGES
# =========================================================

plant_images = {
    "Rose": "images/rose.jpg",
    "Jasmine": "images/jasmine.jpg",
    "Aloe Vera": "images/aloe_vera.jpg",
    "Money Plant": "images/Money_plant.jpg",
    "Hibiscus": "images/hibiscus.jpg",
    "Lotus": "images/lotus.jpg",
    "Marigold": "images/mari_gold.jpg",
    "Sunflower": "images/sunflowe.jpg",
    "Tulip": "images/Tulip.jpg"
}


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("Green Bloom")
st.sidebar.write("Plant Stock Management System")

menu = st.sidebar.selectbox(
    "Select Menu",
    [
        "Home",
        "Plants",
        "Search Plant",
        "Add Plant",
        "Update Quantity",
        "Delete Plant",
        "Supplier Management",
        "Customers",
        "Billing",
        "Reports"
    ]
)


# =========================================================
# HOME
# =========================================================

if menu == "Home":

    st.title("Green Bloom Plants")
    st.subheader("Plant Stock Management System")

    st.write(
        "Welcome to Green Bloom Plant Nursery. "
        "Manage plants, suppliers, customers, billing and reports easily."
    )

    st.markdown("## Our Green World")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(
            "images/rose.jpg",
            caption="Rose",
            width="stretch"
        )

    with col2:
        st.image(
            "images/jasmine.jpg",
            caption="Jasmine",
            width="stretch"
        )

    with col3:
        st.image(
            "images/aloe_vera.jpg",
            caption="Aloe Vera",
            width="stretch"
        )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(
            "images/Money_plant.jpg",
            caption="Money Plant",
            width="stretch"
        )

    with col2:
        st.image(
            "images/hibiscus.jpg",
            caption="Hibiscus",
            width="stretch"
        )

    with col3:
        st.image(
            "images/lotus.jpg",
            caption="Lotus",
            width="stretch"
        )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(
            "images/mari_gold.jpg",
            caption="Marigold",
            width="stretch"
        )

    with col2:
        st.image(
            "images/sunflowe.jpg",
            caption="Sunflower",
            width="stretch"
        )

    with col3:
        st.image(
            "images/Tulip.jpg",
            caption="Tulip",
            width="stretch"
        )

    st.markdown("## About Green Bloom")

    st.info(
        "Green Bloom is a Plant Stock Management System "
        "used to manage plant stock, suppliers, customers, "
        "billing and sales records."
    )


# =========================================================
# PLANTS
# =========================================================

elif menu == "Plants":

    st.title("Plant Stock")

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

            st.markdown(f"### {plant[1]}")

            col1, col2 = st.columns([1, 3])

            with col1:

                image_path = plant_images.get(plant[1])

                if image_path:
                    st.image(
                        image_path,
                        width=200
                    )
                else:
                    st.info("No image available")

            with col2:

                st.write("**Plant ID:**", plant[0])
                st.write("**Plant Name:**", plant[1])
                st.write("**Category:**", plant[2])
                st.write("**Price:**", f"₹{plant[3]}")
                st.write("**Quantity:**", plant[4])
                st.write("**Supplier:**", plant[5])

            st.divider()


# =========================================================
# SEARCH PLANT
# =========================================================

elif menu == "Search Plant":

    st.title("Search Plant")

    search_name = st.text_input(
        "Enter Plant Name"
    )

    if st.button("Search"):

        if search_name.strip() == "":

            st.warning(
                "Please enter a plant name."
            )

        else:

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
                WHERE plant_name LIKE %s
                ORDER BY plant_id
            """, (f"%{search_name}%",))

            plants = cursor.fetchall()

            cursor.close()
            connection.close()

            if len(plants) == 0:

                st.warning("Plant not found.")

            else:

                for plant in plants:

                    st.markdown(
                        f"### {plant[1]}"
                    )

                    col1, col2 = st.columns([1, 3])

                    with col1:

                        image_path = plant_images.get(
                            plant[1]
                        )

                        if image_path:
                            st.image(
                                image_path,
                                width=200
                            )
                        else:
                            st.info(
                                "No image available"
                            )

                    with col2:

                        st.write(
                            "**Plant ID:**",
                            plant[0]
                        )

                        st.write(
                            "**Plant Name:**",
                            plant[1]
                        )

                        st.write(
                            "**Category:**",
                            plant[2]
                        )

                        st.write(
                            "**Price:**",
                            f"₹{plant[3]}"
                        )

                        st.write(
                            "**Quantity:**",
                            plant[4]
                        )

                        st.write(
                            "**Supplier:**",
                            plant[5]
                        )

                    st.divider()


# =========================================================
# ADD PLANT
# =========================================================

elif menu == "Add Plant":

    st.title("Add New Plant")

    plant_id = st.number_input(
        "Plant ID",
        min_value=1,
        step=1
    )

    plant_name = st.text_input(
        "Plant Name"
    )

    category = st.text_input(
        "Category"
    )

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

    supplier_name = st.text_input(
        "Supplier Name"
    )

    if st.button("Add Plant"):

        if (
            plant_name.strip() == ""
            or category.strip() == ""
            or supplier_name.strip() == ""
        ):

            st.warning(
                "Please fill all fields."
            )

        else:

            connection = get_connection()
            cursor = connection.cursor()

            try:

                cursor.execute("""
                    INSERT INTO plants
                    (
                        plant_id,
                        plant_name,
                        category,
                        price,
                        quantity,
                        supplier_name
                    )
                    VALUES
                    (%s, %s, %s, %s, %s, %s)
                """,
                (
                    plant_id,
                    plant_name,
                    category,
                    price,
                    quantity,
                    supplier_name
                ))

                connection.commit()

                st.success(
                    "Plant added successfully."
                )

            except Exception as e:

                connection.rollback()

                st.error(
                    f"Error: {e}"
                )

            finally:

                cursor.close()
                connection.close()


# =========================================================
# UPDATE PLANT QUANTITY
# =========================================================

elif menu == "Update Quantity":

    st.title("Update Plant Quantity")

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

            cursor.execute("""
                UPDATE plants
                SET quantity = %s
                WHERE plant_id = %s
            """,
            (
                new_quantity,
                plant_id
            ))

            connection.commit()

            if cursor.rowcount > 0:

                st.success(
                    "Plant quantity updated successfully."
                )

            else:

                st.warning(
                    "Plant not found."
                )

        except Exception as e:

            connection.rollback()

            st.error(
                f"Error: {e}"
            )

        finally:

            cursor.close()
            connection.close()


# =========================================================
# DELETE PLANT
# =========================================================

elif menu == "Delete Plant":

    st.title("Delete Plant")

    plant_id = st.number_input(
        "Plant ID to Delete",
        min_value=1,
        step=1
    )

    if st.button("Delete Plant"):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            cursor.execute("""
                DELETE FROM plants
                WHERE plant_id = %s
            """,
            (plant_id,))

            connection.commit()

            if cursor.rowcount > 0:

                st.success(
                    "Plant deleted successfully."
                )

            else:

                st.warning(
                    "Plant not found."
                )

        except Exception as e:

            connection.rollback()

            st.error(
                f"Error: {e}"
            )

        finally:

            cursor.close()
            connection.close()


# =========================================================
# SUPPLIER MANAGEMENT
# =========================================================

elif menu == "Supplier Management":

    st.title("Supplier Management")

    supplier_action = st.radio(
        "Select Supplier Operation",
        [
            "View Suppliers",
            "Add Supplier",
            "Update Supplier",
            "Delete Supplier"
        ],
        horizontal=True
    )


    # =====================================================
    # VIEW SUPPLIERS
    # =====================================================

    if supplier_action == "View Suppliers":

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

            st.info(
                "No suppliers available."
            )

        else:

            for supplier in suppliers:

                st.markdown(
                    f"### {supplier[1]}"
                )

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


    # =====================================================
    # ADD SUPPLIER
    # =====================================================

    elif supplier_action == "Add Supplier":

        st.subheader("Add New Supplier")

        supplier_id = st.text_input(
            "Supplier ID"
        )

        supplier_name = st.text_input(
            "Supplier Name"
        )

        phone = st.text_input(
            "Phone"
        )

        city = st.text_input(
            "City"
        )


        if st.button("Add Supplier"):

            if (
                supplier_id.strip() == ""
                or supplier_name.strip() == ""
                or phone.strip() == ""
                or city.strip() == ""
            ):

                st.warning(
                    "Please fill all fields."
                )

            else:

                connection = get_connection()
                cursor = connection.cursor()

                try:

                    cursor.execute("""
                        INSERT INTO suppliers
                        (
                            supplier_id,
                            supplier_name,
                            phone,
                            city
                        )
                        VALUES
                        (%s, %s, %s, %s)
                    """,
                    (
                        supplier_id,
                        supplier_name,
                        phone,
                        city
                    ))

                    connection.commit()

                    st.success(
                        "Supplier added successfully."
                    )

                except Exception as e:

                    connection.rollback()

                    st.error(
                        f"Error: {e}"
                    )

                finally:

                    cursor.close()
                    connection.close()


    # =====================================================
    # UPDATE SUPPLIER
    # =====================================================

    elif supplier_action == "Update Supplier":

        st.subheader("Update Supplier")

        supplier_id = st.text_input(
            "Supplier ID"
        )

        supplier_name = st.text_input(
            "New Supplier Name"
        )

        phone = st.text_input(
            "New Phone"
        )

        city = st.text_input(
            "New City"
        )


        if st.button("Update Supplier"):

            if supplier_id.strip() == "":

                st.warning(
                    "Please enter Supplier ID."
                )

            else:

                connection = get_connection()
                cursor = connection.cursor()

                try:

                    cursor.execute("""
                        UPDATE suppliers
                        SET
                            supplier_name = %s,
                            phone = %s,
                            city = %s
                        WHERE supplier_id = %s
                    """,
                    (
                        supplier_name,
                        phone,
                        city,
                        supplier_id
                    ))

                    connection.commit()

                    if cursor.rowcount > 0:

                        st.success(
                            "Supplier updated successfully."
                        )

                    else:

                        st.warning(
                            "Supplier not found."
                        )

                except Exception as e:

                    connection.rollback()

                    st.error(
                        f"Error: {e}"
                    )

                finally:

                    cursor.close()
                    connection.close()


    # =====================================================
    # DELETE SUPPLIER
    # =====================================================

    elif supplier_action == "Delete Supplier":

        st.subheader("Delete Supplier")

        supplier_id = st.text_input(
            "Supplier ID to Delete"
        )


        if st.button("Delete Supplier"):

            if supplier_id.strip() == "":

                st.warning(
                    "Please enter Supplier ID."
                )

            else:

                connection = get_connection()
                cursor = connection.cursor()

                try:

                    cursor.execute("""
                        DELETE FROM suppliers
                        WHERE supplier_id = %s
                    """,
                    (supplier_id,))

                    connection.commit()

                    if cursor.rowcount > 0:

                        st.success(
                            "Supplier deleted successfully."
                        )

                    else:

                        st.warning(
                            "Supplier not found."
                        )

                except Exception as e:

                    connection.rollback()

                    st.error(
                        f"Error: {e}"
                    )

                finally:

                    cursor.close()
                    connection.close()


# =========================================================
# CUSTOMERS
# =========================================================

elif menu == "Customers":

    st.title("Customers")

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

        st.info(
            "No customers available."
        )

    else:

        for customer in customers:

            st.markdown(
                f"### {customer[1]}"
            )

            col1, col2, col3, col4 = st.columns(4)

            with col1:

                st.write(
                    "**Customer ID**"
                )

                st.write(
                    customer[0]
                )

            with col2:

                st.write(
                    "**Customer Name**"
                )

                st.write(
                    customer[1]
                )

            with col3:

                st.write(
                    "**Phone**"
                )

                st.write(
                    customer[2]
                )

            with col4:

                st.write(
                    "**City**"
                )

                st.write(
                    customer[3]
                )

            st.divider()


        # =================================================
        # CUSTOMER PURCHASE HISTORY
        # =================================================

        st.markdown(
            "## Customer Purchase History"
        )

        customer_names = []

        for customer in customers:

            customer_names.append(
                customer[1]
            )


        if len(customer_names) > 0:

            selected_customer = st.selectbox(
                "Select Customer",
                customer_names
            )


            if st.button(
                "View Purchase History"
            ):

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
                    WHERE customer_name = %s
                    ORDER BY sale_id DESC
                """,
                (selected_customer,))

                history = cursor.fetchall()

                cursor.close()
                connection.close()


                if len(history) == 0:

                    st.info(
                        "No purchases found for this customer."
                    )

                else:

                    total_customer_purchase = 0

                    for sale in history:

                        total_customer_purchase += float(
                            sale[4]
                        )

                        st.markdown(
                            f"### Sale #{sale[0]}"
                        )

                        st.write(
                            "**Plant:**",
                            sale[2]
                        )

                        st.write(
                            "**Quantity:**",
                            sale[3]
                        )

                        st.write(
                            "**Total Amount:**",
                            f"₹{sale[4]:.2f}"
                        )

                        st.write(
                            "**Sale Date:**",
                            sale[5]
                        )

                        st.divider()


                    st.metric(
                        "Customer Total Purchase",
                        f"₹{total_customer_purchase:.2f}"
                    )


# =========================================================
# BILLING
# =========================================================

elif menu == "Billing":

    st.title("Green Bloom Billing")

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

        st.warning(
            "No plants available for sale."
        )

    else:

        customer_name = st.text_input(
            "Customer Name"
        )


        plant_names = []

        for plant in plants:

            plant_names.append(
                plant[0]
            )


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


        image_path = plant_images.get(
            selected_plant
        )

        if image_path:

            st.image(
                image_path,
                caption=selected_plant,
                width=250
            )


        st.write(
            "**Price:**",
            f"₹{price}"
        )

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


        total_amount = (
            price * sale_quantity
        )


        st.markdown(
            "### Total Amount"
        )

        st.write(
            f"## ₹{total_amount:.2f}"
        )


        if st.button(
            "Generate Bill"
        ):

            if customer_name.strip() == "":

                st.warning(
                    "Please enter customer name."
                )

            else:

                connection = get_connection()
                cursor = connection.cursor()

                try:

                    cursor.execute("""
                        INSERT INTO sales
                        (
                            customer_name,
                            plant_name,
                            quantity,
                            total_amount,
                            sale_date
                        )
                        VALUES
                        (%s, %s, %s, %s, %s)
                    """,
                    (
                        customer_name,
                        selected_plant,
                        sale_quantity,
                        total_amount,
                        date.today()
                    ))


                    cursor.execute("""
                        UPDATE plants
                        SET quantity = quantity - %s
                        WHERE plant_name = %s
                        AND quantity >= %s
                    """,
                    (
                        sale_quantity,
                        selected_plant,
                        sale_quantity
                    ))


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
                            "## Green Bloom Bill"
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
                            "Thank you for shopping with Green Bloom!"
                        )


                except Exception as e:

                    connection.rollback()

                    st.error(
                        f"Error: {e}"
                    )


                finally:

                    cursor.close()
                    connection.close()


# =========================================================
# REPORTS
# =========================================================

elif menu == "Reports":

    st.title("Green Bloom Reports")


    report_type = st.selectbox(
        "Select Report",
        [
            "Total Sales",
            "Available Stock",
            "Low Stock Plants",
            "Customer Purchase History"
        ]
    )


    # =====================================================
    # TOTAL SALES
    # =====================================================

    if report_type == "Total Sales":

        st.subheader(
            "Total Sales Report"
        )

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

            st.info(
                "No sales available."
            )

        else:

            total_sales = 0

            for sale in sales:

                total_sales += float(
                    sale[4]
                )


            st.metric(
                "Total Sales",
                f"₹{total_sales:.2f}"
            )

            st.markdown("---")


            for sale in sales:

                st.markdown(
                    f"### Sale #{sale[0]}"
                )

                col1, col2, col3 = st.columns(3)


                with col1:

                    st.write(
                        "**Customer:**",
                        sale[1]
                    )

                    st.write(
                        "**Plant:**",
                        sale[2]
                    )


                with col2:

                    st.write(
                        "**Quantity:**",
                        sale[3]
                    )

                    st.write(
                        "**Total Amount:**",
                        f"₹{sale[4]:.2f}"
                    )


                with col3:

                    st.write(
                        "**Sale Date:**",
                        sale[5]
                    )


                st.divider()


    # =====================================================
    # AVAILABLE STOCK
    # =====================================================

    elif report_type == "Available Stock":

        st.subheader(
            "Available Stock Report"
        )

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

            st.info(
                "No stock available."
            )

        else:

            for plant in plants:

                st.markdown(
                    f"### {plant[1]}"
                )

                st.write(
                    "**Plant ID:**",
                    plant[0]
                )

                st.write(
                    "**Category:**",
                    plant[2]
                )

                st.write(
                    "**Price:**",
                    f"₹{plant[3]}"
                )

                st.write(
                    "**Available Quantity:**",
                    plant[4]
                )

                st.write(
                    "**Supplier:**",
                    plant[5]
                )

                st.divider()


    # =====================================================
    # LOW STOCK
    # =====================================================

    elif report_type == "Low Stock Plants":

        st.subheader(
            "Low Stock Plants Report"
        )

        st.write(
            "Plants with quantity less than or equal to 10."
        )

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
            WHERE quantity <= 10
            ORDER BY quantity
        """)

        low_stock = cursor.fetchall()

        cursor.close()
        connection.close()


        if len(low_stock) == 0:

            st.success(
                "No low stock plants."
            )

        else:

            for plant in low_stock:

                st.markdown(
                    f"### {plant[1]}"
                )

                st.write(
                    "**Plant ID:**",
                    plant[0]
                )

                st.write(
                    "**Category:**",
                    plant[2]
                )

                st.write(
                    "**Price:**",
                    f"₹{plant[3]}"
                )

                st.write(
                    "**Quantity:**",
                    plant[4]
                )

                st.write(
                    "**Supplier:**",
                    plant[5]
                )

                st.divider()


    # =====================================================
    # CUSTOMER PURCHASE HISTORY
    # =====================================================

    elif report_type == "Customer Purchase History":

        st.subheader(
            "Customer Purchase History"
        )

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT DISTINCT customer_name
            FROM sales
            ORDER BY customer_name
        """)

        customer_data = cursor.fetchall()

        cursor.close()
        connection.close()


        if len(customer_data) == 0:

            st.info(
                "No customer purchase records."
            )

        else:

            customer_names = []

            for customer in customer_data:

                customer_names.append(
                    customer[0]
                )


            selected_customer = st.selectbox(
                "Select Customer",
                customer_names
            )


            if st.button(
                "Show Customer Purchases"
            ):

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
                    WHERE customer_name = %s
                    ORDER BY sale_id DESC
                """,
                (selected_customer,))

                history = cursor.fetchall()

                cursor.close()
                connection.close()


                if len(history) == 0:

                    st.info(
                        "No purchases found."
                    )

                else:

                    total_purchase = 0

                    for sale in history:

                        total_purchase += float(
                            sale[4]
                        )

                        st.markdown(
                            f"### Sale #{sale[0]}"
                        )

                        st.write(
                            "**Customer:**",
                            sale[1]
                        )

                        st.write(
                            "**Plant:**",
                            sale[2]
                        )

                        st.write(
                            "**Quantity:**",
                            sale[3]
                        )
