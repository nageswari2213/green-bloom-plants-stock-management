from db_connection import get_connection


def show_sales_report():

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

    print("\n========== SALES REPORT ==========")

    if len(sales) == 0:

        print("No sales available.")

    else:

        for sale in sales:

            print("Sale ID       :", sale[0])
            print("Customer Name :", sale[1])
            print("Plant Name    :", sale[2])
            print("Quantity      :", sale[3])
            print("Total Amount  :", sale[4])
            print("Sale Date     :", sale[5])
            print("-----------------------------------")

    cursor.close()
    connection.close()
