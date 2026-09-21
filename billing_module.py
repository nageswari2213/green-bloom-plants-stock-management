from db_connection import get_connection
from datetime import date


def generate_bill(customer_name, plant_name, quantity):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT price, quantity
        FROM plants
        WHERE plant_name = %s
        """,
        (plant_name,)
    )

    plant = cursor.fetchone()

    if plant is None:

        print("Plant not found.")

        cursor.close()
        connection.close()
        return

    price = plant[0]
    available_quantity = plant[1]

    if quantity <= 0:

        print("Quantity must be greater than 0.")

        cursor.close()
        connection.close()
        return

    if quantity > available_quantity:

        print("Insufficient stock.")

        cursor.close()
        connection.close()
        return

    total_amount = price * quantity

    try:

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
                plant_name,
                quantity,
                total_amount,
                date.today()
            )
        )

        cursor.execute(
            """
            UPDATE plants
            SET quantity = quantity - %s
            WHERE plant_name = %s
            AND quantity >= %s
            """,
            (
                quantity,
                plant_name,
                quantity
            )
        )

        if cursor.rowcount == 0:

            connection.rollback()
            print("Unable to update stock.")

        else:

            connection.commit()

            print("\n========== GREEN BLOOM BILL ==========")
            print("Customer Name :", customer_name)
            print("Plant Name    :", plant_name)
            print("Quantity      :", quantity)
            print("Price         :", price)
            print("Total Amount  :", total_amount)
            print("Date          :", date.today())
            print("--------------------------------------")

    except Exception as e:

        connection.rollback()
        print("Error:", e)

    finally:

        cursor.close()
        connection.close()
