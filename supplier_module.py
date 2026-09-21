from db_connection import get_connection


def show_suppliers():

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

    print("\n========== SUPPLIER DETAILS ==========")

    if len(suppliers) == 0:
        print("No suppliers available.")

    else:

        for supplier in suppliers:

            print("Supplier ID   :", supplier[0])
            print("Supplier Name :", supplier[1])
            print("Phone         :", supplier[2])
            print("City          :", supplier[3])
            print("-----------------------------------")

    cursor.close()
    connection.close()

