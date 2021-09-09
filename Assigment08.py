# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# ARonsse,9.4.2021,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []  # declares list
strChoice = ""  # captures user menu selection


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name
        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        ARonsse, 9.4.2021 ,Modified code to complete assignment 8
    """

    # -- Constructor --
    def __init__(self, product_name, product_price):
        self.__product_name = product_name
        self.__product_price = product_price

    # -- Properties --
    @property
    def product_name(self):  # (getter)
        return str(self.__product_name)

    @product_name.setter
    def product_name(self, value):  # (setter)
        if not str(value).isnumeric():
            self.__product_name = value
        else:
            raise Exception("Product name must include letters.")

    @property
    def product_price(self):  # (getter)
        return str(self.__product_price)

    @product_price.setter
    def product_price(self, value):  # (setter)
        try:
            self.__product_price = float(value)
        except TypeError:
            print("Product price must not include letters or symbols.")

    # -- Methods --
    def to_string(self):
        return self.__str__()

    def __str__(self):
        return self.product_name + ',' + self.product_price


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):
        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        ARonsse, 9.4.2021,Modified code to complete assignment 8
    """

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ Saves data in list to file

        :param file_name: (string) with name of file:
        :param list_of_product_objects: (list) with object instance data:
        :return: (list) of dictionary rows
        """
        file = open(file_name, 'w')
        for obj in list_of_product_objects:
            file.write(obj + '\n')
        file.close()

    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list of object instances

        :param file_name: (string) with name of file:
        :return: (list) with object instance data
        """
        file = open(file_name, "r")
        list_of_product_objects = []
        for line in file:
            product_name, product_price = line.split(',')
            product_object = (product_name.lstrip().rstrip(), product_price.lstrip().rstrip())
            list_of_product_objects.append(product_object)
        file.close()
        return list_of_product_objects


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        MENU
        1) Add Product Data
        2) View Current Data
        3) Save Data to File       
        4) Exit Program
        ''')
        print()

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()
        return choice

    @staticmethod
    def input_new_product():
        """ Collect new product information from the user

        :param: none
        :return: product_name, product_price
        """
        product_name = input('Enter a product name: ').strip()
        product_price = input('What is the price of this item?: ').strip()
        return product_name, product_price

    @staticmethod
    def print_current_data(list_of_product_objects):
        """ Shows the product data in the lsit

        :param list_of_product_objects: (list) of data to display
        :return: nothing
        """
        print("******* The current products logged are: *******")
        if list_of_product_objects == []:
            print("No products logged. Select option 1 on the menu to add a product.")
        else:
            for obj in list_of_product_objects:
                print(obj)
        print("*******************************************")
        print()


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of product objects when script starts
# lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)
try:
    lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)
    print("File load successful!")
    IO.print_current_data(lstOfProductObjects)
except:
    print("No existing file found. Add product data and save to create a product log.")

while (True):
    IO.print_menu()  # Shows user a menu of options
    strChoice = IO.input_menu_choice()  # Gets user's menu option choice

    if strChoice.strip() == '1':  # Add a new product
        product_data = IO.input_new_product()  # Requests user input and captures function output
        name, price = product_data  # Unpack the tuple
        productObject = Product(name, price).to_string()  # Pass arguments into class attribute
        lstOfProductObjects.append(productObject)
        continue

    elif strChoice.strip() == '2':  # view existing data
        IO.print_current_data(lstOfProductObjects)
        continue

    elif strChoice.strip() == '3':  # save to file
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        print("File saved!")
        continue

    elif strChoice.strip() == '4':  # exit
        print("Goodbye!")
        break

# Main Body of Script  ---------------------------------------------------- #
