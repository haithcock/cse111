import csv

'''
In receipt.py, write a function named
 read_dictionary that will open a 
CSV file for reading and use a 
csv.reader to read each row and 
populate a compound dictionary with the 
contents of the products.csv file. 
The read_dictionary function must 
have this header and documentation string: 

'''
def main():
       



    PRODUCT_NUM_INDEX = 0
    PRODUCT_NAME_INDEX = 1
    PRODUCT_PRICE_INDEX = 2
    product_dict = read_dictionary("products.csv", PRODUCT_NUM_INDEX)
    print(product_dict)
    request_list=[]
    with open("request.csv", "rt") as request_file:
        reader = csv.reader(request_file)
        next(reader)  # Skip header row

        for row in reader:
            if len(row) != 0:  # Ensure row is not empty
                product_number = row[0]  # Extract product number
                quantity = int(row[1])   # Extract requested quantity

                # Append each row as a list to the request_list
                request_list.append([product_number, quantity])
                if product_number in product_dict:
                    product_info = product_dict[product_number]
                    product_name = product_info[PRODUCT_NAME_INDEX]
                    product_price = float(product_info[PRODUCT_PRICE_INDEX])
                
                    print(f"{product_name}: {quantity} @ ${product_price:.2f} each")
                else:
                    print(f"Error: Product {product_number} not found in products.csv")

    
()

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
dictionary and return the dictionary.
Parameters
    filename: the name of the CSV file to read.
    key_column_index: the index of the column
        to use as the keys in the dictionary.
Return: a compound dictionary that contains
    the contents of the CSV file.
"""
    
    dictionary ={}
    with open (filename, "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row_list in reader:
                    if len(row_list) != 0:
                        key = row_list[key_column_index]
                        dictionary[key] = row_list
    return dictionary
   
if __name__ == "__main__":  
    main()

