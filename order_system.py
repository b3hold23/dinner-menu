def get_quantity(item_name, quantity=None):
    while True:
        try:
            quantity = int(quantity if quantity is not None else input(f"How many {item_name} would you like to order? "))
            if quantity < 1:
                print("Please enter a valid quantity.")
                continue
            return quantity
        except ValueError:
            print("Please enter a number.")


def place_order(menu):
    """
    Displays a restaurant menu, asks customers for their order, then returns
    their receipt and total price.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their 
                       prices, using the following format:
                        {
                            "Food category": {
                                "Meal": price
                            }
                        }

    Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                  and quantity ordered.
    order_total (float): The total price of the order.
    """
    order = []
    item_list = []

    # Map menu items to numbers with formatted names and prices.
    for category, items in menu.items():
        for meal, price in items.items():
            full_name = f"{category} - {meal}"
            item_list.append({"name": full_name, "price": price})

    # Greeting and formatted menu header.
    print("Welcome to the Generic Take Out Restaurant.")
    print("What would you like to order? ")
    print("--------------------------------------------------")
    print("Item # | Item name                        | Price")
    print("-------|----------------------------------|-------")

    # Display items in a table format with alignment.
    for i, item in enumerate(item_list, start=1):
        print(f"{i:<7} | {item['name']:<32} | ${item['price']:.2f}")

    while True:
        try:
            order_index = int(input("Type menu number: "))
            if order_index == 0:
                break
            if order_index < 1 or order_index > len(item_list):
                print("Please enter a valid number.")
                continue
        except ValueError:
            print("Please enter a number.")
            continue
        
        selected_item = item_list[order_index - 1]
        quantity = get_quantity(selected_item["name"])

        # Add selected item to order.
        order.append({
            "Item name": selected_item['name'],
            "Price": selected_item['price'],
            "Quantity": quantity
        })

        order_more = input("Would you like to keep ordering? (N) to quit: ").strip().lower()
        if order_more != "y":
            break

    # Calculate total and print formatted receipt.
    order_total = round(sum([item['Price'] * item['Quantity'] for item in order]), 2)
    return order, order_total

def update_order(order, menu_selection, item_list):
    """
    Checks if the customer menu selection is valid, then updates the order.

    Parameters:
    order (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered.
    menu_selection (str): The customer's menu selection.
    item_list (dictionary): A dictionary containing the menu items and their
                            prices.

    Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered (updated as needed).
    """  
    try:
        menu_selection = int(menu_selection)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return order
    if 1 <= menu_selection <= len(item_list):
        item_name = list(item_list.keys())[menu_selection - 1]
        item_price = item_list[item_name]['Price']

        try:
            quantity = int(input(f"How many {item_name} would you like to order? "))
            if quantity < 1:
                print("Quantity must be at least 1.")
                quantity = 1
        except ValueError:
            print("Invalid input. Quantity must be a number.")
            quantity = 1

        order.append({
            "Item name": item_name,
            "Price": item_price,
            "Quantity": quantity
        })
        print(f"{quantity} {item_name} added to your order.")
    else:
        print("Invalid input. Please enter a valid number.")   
    return order
def print_itemized_receipt(receipt):
    """
    Prints an itemized receipt for the customer.

    Parameters:
    receipt (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered.
    """
    # Uncomment the following line if you need to check the structure of the receipt

    total_price = 0.0

    for item in receipt:
        item_name = item.get("Item name")
        price = item.get("Price")
        quantity = item.get("Quantity")

        print_receipt_line(item_name, price, quantity)

        total_price += price * quantity


##################################################
#  STARTER CODE
#  Do not modify any of the code below this line:
##################################################

def print_receipt_line(item_name, price, quantity):
    """
    Prints a line of the receipt.

    Parameters:
    item_name (str): The name of the meal item.
    price (float): The price of the meal item.
    quantity (int): The quantity of the meal item.
    """
    # Calculate the number of spaces for formatted printing
    num_item_spaces = 32 - len(item_name)
    num_price_spaces = 6 - len(str(price))

    # Create space strings
    item_spaces = " " * num_item_spaces
    price_spaces = " " * num_price_spaces

    # Print the item name, price, and quantity
    print(f"{item_name}{item_spaces}| ${price}{price_spaces}| {quantity}")

def print_receipt_heading():
    """
    Prints the receipt heading.
    """
    print("----------------------------------------------------")
    print("Item name                       | Price  | Quantity")
    print("--------------------------------|--------|----------")

def print_receipt_footer(total_price):
    """
    Prints the receipt footer with the total price of the order.

    Parameters:
    total_price (float): The total price of the order.
    """
    print("----------------------------------------------------")
    print(f"Total price: ${total_price:.2f}")
    print("----------------------------------------------------")

def print_menu_heading():
    """
    Prints the menu heading.
    """
    print("--------------------------------------------------")
    print("Item # | Item name                        | Price")
    print("-------|----------------------------------|-------")

def print_menu_line(index, food_category, meal, price):
    """
    Prints a line of the menu.

    Parameters:
    index (int): The menu item number.
    food_category (str): The category of the food item.
    meal (str): The name of the meal item.
    price (float): The price of the meal item.
    """
    # Print the menu item number, food category, meal, and price
    num_item_spaces = 32 - len(food_category + meal) - 3
    item_spaces = " " * num_item_spaces
    if index < 10:
        i_spaces = " " * 6
    else:
        i_spaces = " " * 5
    print(f"{index}{i_spaces}| {food_category} - {meal}{item_spaces} | ${price}")

def get_menu_items_dict(menu):
    """
    Creates a dictionary of menu items and their prices mapped to their menu 
    number.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their
                        prices.

    Returns:
    item_list (dictionary): A dictionary containing the menu items and their
                            prices.
    """
    # Create an empty dictionary to store the menu items
    item_list = {}

    # Create a variable for the menu item number
    i = 1

    # Loop through the menu dictionary
    for food_category, options in menu.items():
        # Loop through the options for each food category
        for meal, price in options.items():
            # Store the menu item number, item name and price in the item_list
            item_list[i] = {
                "Item name": food_category + " - " + meal,
                "Price": price
            }
            i += 1

    return item_list

def get_menu_dictionary():
    """
    Returns a dictionary of menu items and their prices.

    Returns:
    meals (dictionary): A nested dictionary containing the menu items and their
                        prices in the following format:
                        {
                            "Food category": {
                                "Meal": price
                            }
                        }
    """
    # Create a meal menu dictionary
    #"""
    meals = {
        "Burrito": {
            "Chicken": 4.49,
            "Beef": 5.49,
            "Vegetarian": 3.99
        },
        "Rice Bowl": {
            "Teriyaki Chicken": 9.99,
            "Sweet and Sour Pork": 8.99
        },
        "Sushi": {
            "California Roll": 7.49,
            "Spicy Tuna Roll": 8.49
        },
        "Noodles": {
            "Pad Thai": 6.99,
            "Lo Mein": 7.99,
            "Mee Goreng": 8.99
        },
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    }
    """
    # This menu is just for testing purposes
    meals = {
        "Cake": {
            "Kuih Lapis": 3.49,
            "Strawberry Cheesecake": 6.49,
            "Chocolate Crepe Cake": 6.99
        },
        "Pie": {
            "Apple": 4.99,
            "Lemon Meringue": 5.49
        },
        "Ice-cream": {
            "2-Scoop Vanilla Cone": 3.49,
            "Banana Split": 8.49,
            "Chocolate Sundae": 6.99
        }
    }
    """
    return meals

# Run the program
if __name__ == "__main__":
    # Get the menu dictionary
    meals = get_menu_dictionary()

    receipt, total_price = place_order(meals)

    # Print out the customer's order
    print("This is what we are preparing for you.\n")

    # Print the receipt heading
    print_receipt_heading()

    # Print the customer's itemized receipt
    print_itemized_receipt(receipt)

    # Print the receipt footer with the total price
    print_receipt_footer(total_price)

