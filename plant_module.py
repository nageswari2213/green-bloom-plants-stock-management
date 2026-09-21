from db_connection import get_connection


def show_plants():

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

    print("\n========== PLANT DETAILS ==========")

    if len(plants) == 0:
        print("No plants available.")

    else:

        for plant in plants:

            print("Plant ID      :", plant[0])
            print("Plant Name    :", plant[1])
            print("Category      :", plant[2])
            print("Price         :", plant[3])
            print("Quantity      :", plant[4])
            print("Supplier Name :", plant[5])
            print("-----------------------------------")

    cursor.close()
    connection.close()
