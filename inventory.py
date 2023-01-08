# Import required modules
import tabulate # Do pip install tabulate before this program

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.get_cost

    def get_quantity(self):
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        '''
        Add a code to returns a string representation of a class.
        '''
        return f"Origin of Country: {self.country} \nCode: {self.code}\nProduct Name: {self.product}\nCost: {self.cost}\nQuantity: {self.quantity}"


def get_shoe_from_line(line):
    """
    This function is to separate the input line into various variables
    and then put the variables into Shoe constructor
    to create an object shoe

    Parameters
    ----------
    line : str
        a string of line separated by comma

    Return
    ------
    Shoe
        an object of Shoe
    """
    record = line.split(",")
    country = record[0].strip()
    code = record[1].strip()
    product = record[2].strip()
    cost = float(record[3].strip())
    quantity = int(record[4].strip())
    return Shoe(country, code, product, cost, quantity)

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
global shoe_list
shoe_list = list()

#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    shoe_list.clear() # Intialise shoe_list to empty
    try:
        # Read the file into a list of str
        inventory_lines = []
        with open("inventory.txt" , 'r') as file_reader:
            inventory_lines = file_reader.readlines()
        
        # Read each line to capture values separated by comma, then print in a defined format
        # Skip the first line which is the header
        for inventory_line in inventory_lines[1:]:
            shoe = get_shoe_from_line(inventory_line)
            shoe_list.append(shoe)

        # Print a message when finish
        print(f"Shoe records are read. There are {len(shoe_list)} shoe records in the inventory.")
    except Exception:
        # In case of any error, print an error message and result in an empty list
        print("Error in reading the file.")
        shoe_list.clear()

def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    while True:
        try:
            # Ask user to enter the details of the shoe
            country = input("Please enter the origin of the country: ")
            code = input("Please enter the code: ")
            product = input("Please enter the product: ") 
            cost = float(input("Please enter the cost: "))
            quantity = int(input("Please enter quantity: "))
            new_shoe = Shoe(country, code, product, cost, quantity)
            shoe_list.append(new_shoe)

            # Append the new record into the file
            with open("inventory.txt", "a") as file:
                file.write(f"\n{country},{code},{product},{cost},{quantity}")

            # Print when done
            print(f"New shoe \n{new_shoe} has been saved. There are {len(shoe_list)} shoe records in the inventory.")

            # Ask if the user wants to add another shoe information
            add_shoe = input("Do you have another shoe's information to add? Y/N: ").upper()
            if add_shoe == "N":
                break
        except Exception:
            print("Error in capturing new shoes! Please enter again.")

def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    if len(shoe_list) == 0:
        print("No shoe in the inventory. Maybe you should read shoes data first.")
    else:
        # Prepare data list for tabulate
        shoe_data_list = list()
        for shoe in shoe_list:
            data_list = [
                shoe.country,
                shoe.code,
                shoe.product,
                shoe.cost,
                shoe.quantity
            ]
            shoe_data_list.append(data_list)
        header_list = ["Country", "Code", "Product", "Cost", "Quantity"]

        # Print the tabulate table
        print("=== List all shoes ===")
        print(tabulate.tabulate(shoe_data_list, headers=header_list, tablefmt='orgtbl'))

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    if len(shoe_list) == 0:
        print("No shoe is available for re-stock. Maybe you should read shoes data first.")
    else:
        # First of all, find the shoe of the lowest quantity
        lowest_shoe_index = -1
        lowest_quantity = -1
        for index, shoe in enumerate(shoe_list):
            if lowest_shoe_index == -1 or shoe.quantity < lowest_quantity:
                lowest_shoe_index = index
                lowest_quantity = shoe.quantity
        # Ask the user to re-stock
        print(f"The shoe of the lowest quantity is: {shoe_list[lowest_shoe_index]}")

        # Ask the user if they want to re-stock
        want_to_restock = input("Do you want to add more stock? (Y/N) ").upper()
        if want_to_restock == 'Y':
            # Proceed if the user wants to re-stock
            added_quantity = 0
            while True:
                try:
                    added_quantity = int(input("How many shoes more do you want to add? "))
                    if added_quantity <= 0:
                        print("Invalid quantity. Please enter again.")
                    else:
                        break
                except Exception:
                    print("Invalid input. Please enter again")
            # Amend the lowest quantity to the added one
            new_quantity = lowest_quantity + added_quantity
            shoe_list[lowest_shoe_index].quantity = new_quantity
            # Save the list into the file
            with open("inventory.txt", "w") as file_writer:
                # Save header on the first line
                file_writer.write("Country,Code,Product,Cost,Quantity\n")
                for shoe in shoe_list:
                    file_writer.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
            print("Re-stock record is saved.")

def seach_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    if len(shoe_list) == 0:
        print("No shoe record can be searched. Maybe you should read shoes data first.")
    else:
        input_code = input("Which shoe code do you search? ")
        found = False
        for shoe in shoe_list:
            if shoe.code.upper() == input_code.upper():
                print("Searched record:")
                print(shoe)
                found = True
        if found == False:
            print("Given code cannot be found.")

def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    if len(shoe_list) == 0:
        print("No shoe in the inventory. Maybe you should read shoes data first.")
    else:
        # Prepare data list for tabulate
        shoe_data_list = list()
        for shoe in shoe_list:
            data_list = [
                shoe.code,
                shoe.cost * shoe.quantity
            ]
            shoe_data_list.append(data_list)
        header_list = ["Code", "Total Value"]

        # Print the tabulate table
        print("=== List value per item ===")
        print(tabulate.tabulate(shoe_data_list, headers=header_list, tablefmt='orgtbl'))

def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    if len(shoe_list) == 0:
        print("No shoe in the inventory. Maybe you should read shoes data first.")
    else:
        # First of all, find the shoe of the highest quantity
        highest_shoe_index = -1
        highest_quantity = -1
        for index, shoe in enumerate(shoe_list):
            if highest_shoe_index == -1 or shoe.quantity > highest_quantity:
                highest_shoe_index = index
                highest_quantity = shoe.quantity
        # Shoe the result
        print(f"The shoe of the highest quantity is: {shoe_list[highest_shoe_index]}")
        print("This shoe being for sale.")

def print_main_menu():
    print('''=== T32 Inventory Program ===
a. Read shoes data
b. Capture shoes
c. View all shoes
d. Re-stock shoes
e. Search shoes
f. List value per item
g. Highest quantity
q. Quit
''')

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
user_input = ""
while user_input != 'q':
    print_main_menu()
    user_input = input("Please select an option: ").lower()
    if user_input == 'a':
        read_shoes_data()
    elif user_input == 'b':
        capture_shoes()
    elif user_input == 'c':
        view_all()
    elif user_input == 'd':
        re_stock() 
    elif user_input == 'e':
        seach_shoe()  
    elif user_input == 'f':
        value_per_item()
    elif user_input == 'g':
        highest_qty()          
    elif user_input == 'q':
        print("Goodbye...")
        break
    else:
        print("Invalid option! Please enter again.")

