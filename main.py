from plant_module import show_plants
from supplier_module import show_suppliers
from customer_module import show_customers
from billing_module import generate_bill
from reports_module import show_sales_report


def main():

    while True:

        print("\n========== GREEN BLOOM ==========")
        print("1. View Plants")
        print("2. View Suppliers")
        print("3. View Customers")
        print("4. Generate Bill")
        print("5. Sales Report")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_plants()

        elif choice == "2":
            show_suppliers()

        elif choice == "3":
            show_customers()

        elif choice == "4":

            customer_name = input("Enter customer name: ")
            plant_name = input("Enter plant name: ")

            try:
                quantity = int(input("Enter quantity: "))

                generate_bill(
                    customer_name,
                    plant_name,
                    quantity
                )

            except ValueError:
                print("Please enter a valid quantity.")

        elif choice == "5":
            show_sales_report()

        elif choice == "6":
            print("Thank you for using Green Bloom!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()