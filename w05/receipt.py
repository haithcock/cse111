import csv
import random
from datetime import datetime

def main():
    PRODUCT_NUM_INDEX = 0
    PRODUCT_NAME_INDEX = 1
    PRODUCT_PRICE_INDEX = 2
    sales_tax_rate = 0.06  # 6% sales tax
    discount_rate = 0.05   # 5% discount
    discount_chance = 0.10  # 10% probability of winning

    product_dict = read_dictionary("products.csv", PRODUCT_NUM_INDEX)
    print(product_dict)

    with open("request.csv", "rt") as request_file:
        reader = csv.reader(request_file)
        next(reader)  # Skip header row

        for row in reader:
            if len(row) != 0:  # Ensure row is not empty
                total_order_cost = 0  # Initialize total cost for this order

                product_number = row[0]  # Extract product number
                quantity = int(row[1])   # Extract requested quantity

                if product_number in product_dict:
                    product_info = product_dict[product_number]
                    product_name = product_info[PRODUCT_NAME_INDEX]
                    product_price = float(product_info[PRODUCT_PRICE_INDEX])

                    subtotal = product_price * quantity
                    total_order_cost += subtotal  # Sum up this order's total

                    print(f"{product_name}: {quantity} @ ${product_price:.2f} each (Subtotal: ${subtotal:.2f})")
                else:
                    print(f"Error: Product {product_number} not found in products.csv")

                # Apply random discount if eligible
                discount_applied = False
                discount_amount = 0
                if random.random() < discount_chance:  # 10% chance to win
                    discount_amount = total_order_cost * discount_rate
                    total_order_cost -= discount_amount
                    discount_applied = True

                # Compute sales tax and total amount due
                sales_tax = total_order_cost * sales_tax_rate
                total_due = total_order_cost + sales_tax

                # Print subtotal, discount (if applicable), tax, and total due
                print(f"Subtotal: ${total_order_cost + discount_amount:.2f}")
                if discount_applied:
                    print(f"🎉 Congratulations! You won a 5% discount! You saved ${discount_amount:.2f} 🎉")
                print(f"Sales Tax (6%): ${sales_tax:.2f}")
                print(f"Total Amount Due: ${total_due:.2f}\n")

    try:
        # Print a thank you message
        print("\nThank you for shopping with us!")

        # Get and print the current date and time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Current Date and Time: {current_time}")

    except FileNotFoundError:
        print("Error: One or more required files (products.csv or request.csv) were not found.")
    except PermissionError:
        print("Error: Permission denied when trying to access the file.")
    except KeyError as e:
        print(f"Error: Missing expected data in products.csv. Key not found: {e}")

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    
    Parameters:
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.

    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    
    dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header row
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list
    return dictionary

if __name__ == "__main__":  
    main()







