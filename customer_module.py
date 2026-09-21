from db_connection import get_connection


def show_customers():

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

    print("\n========== CUSTOMER DETAILS ==========")

    if len(customers) == 0:
        print("No customers available.")

    else:

        for customer in customers:

            print("Customer ID   :", customer[0])
            print("Customer Name :", customer[1])
            print("Phone         :", customer[2])
            print("City          :", customer[3])
            print("-----------------------------------")

    cursor.close()
    connection.close()

