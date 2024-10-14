# My Shopping App...

print("Welcome to the Devkinandan's Marketplace!")

#DataBase...

users = [{'user_name' : 'username' , 'password' : 'Password'}]

admin = {'admin_user_name' : 'admin_access' , 'admin_password' : 'Password'}

category_ids = [{
    1: 'Fruits',
    2: 'Vegetables',
    3: 'Groceries',
    4: 'Sweets',
    5: 'Bakery'
}]

categories = {

    'Fruits': [
        {'product_id': 1, 'name': 'Apples', 'category_id': 1, 'price': 100.00},
        {'product_id': 2, 'name': 'Mangoes', 'category_id': 1, 'price': 60.00},
        {'product_id': 3, 'name': 'Oranges', 'category_id': 1, 'price': 80.00},
        {'product_id': 4, 'name': 'Grapes', 'category_id': 1, 'price': 50.00},
        {'product_id': 5, 'name': 'Bananas', 'category_id': 1, 'price': 30.00}
    ],

    'Vegetables': [
        {'product_id': 1, 'name': 'Onions', 'category_id': 2, 'price': 100.00},
        {'product_id': 2, 'name': 'Tomatoes', 'category_id': 2, 'price': 60.00},
        {'product_id': 3, 'name': 'Beans', 'category_id': 2, 'price': 80.00},
        {'product_id': 4, 'name': 'Potatoes', 'category_id': 2, 'price': 50.00},
        {'product_id': 5, 'name': 'Pumpkins', 'category_id': 2, 'price': 30.00}
    ],

    'Groceries': [
        {'product_id': 1, 'name': 'Atta', 'category_id': 3, 'price': 100.00},
        {'product_id': 2, 'name': 'Dal', 'category_id': 3, 'price': 60.00},
        {'product_id': 3, 'name': 'Rice', 'category_id': 3, 'price': 80.00},
        {'product_id': 4, 'name': 'Cornflakes', 'category_id': 3, 'price': 50.00},
        {'product_id': 5, 'name': 'Tomato Sauce', 'category_id': 3, 'price': 30.00}
    ],

    'Sweets': [
        {'product_id': 1, 'name': 'Rasgulla', 'category_id': 4, 'price': 100.00},
        {'product_id': 2, 'name': 'Gullab Jamun', 'category_id': 4, 'price': 60.00},
        {'product_id': 3, 'name': 'Laddu', 'category_id': 4, 'price': 80.00},
        {'product_id': 4, 'name': 'Kheermohan', 'category_id': 4, 'price': 50.00},
        {'product_id': 5, 'name': 'Kheerkadam', 'category_id': 4, 'price': 30.00}
    ] ,

    'Bakery': [ 
        {'product_id': 1, 'name': 'Cakes', 'category_id': 5, 'price': 100.00},
        {'product_id': 2, 'name': 'Pastries', 'category_id': 5, 'price': 60.00},
        {'product_id': 3, 'name': 'Patties', 'category_id': 5, 'price': 80.00},
        {'product_id': 4, 'name': 'Cols coffee', 'category_id': 5, 'price': 50.00},
        {'product_id': 5, 'name': 'Cheese Cake', 'category_id': 5, 'price': 30.00}
    ]
}

cart = []

Payments = [{'1' : 'Unified Payment Interface', '2' : 'Debit Card/Credit Card', '3' : 'Net Banking', '4' : 'Cash On Delivery'}]

#Sign Ups...
#this function takes new username and password for signing up of new customers.
#user counter iterates over the Users list and if the key of users indicates username exists error prints and return value is false
# else new user is added via append method.
def add_user(username ,password,user_type):
    for user in users:   #here for loop is used so that i can iterate overthe given list and add users and error does not occur. 
                         #If it was a dirctory direct if else would have worked.
        if user['user_name'] == username:          # this user['user_name'] takes key not value...
            print("Error! User already exists.")
            return False
        else:
            users.append({'user_name' == username , 'password' == password})
            print(f'User {username} successfully added.')
            return True
    if user_type == admin:
        print("Error: Admins cannot be a user.")
        return
        
#Admin login...
# this function takes admin username and password for Logging in of Admin Account that controls the application.
# the if statement targets admin directory looking for right key and its value for both admin username and passwords. 
# If true access granted. the else statement gives access denied as the only credentials were entered wrong.
def admin_login(admin_access , Password):
    if admin['admin_user_name'] == admin_access and admin['admin_password'] == Password:
        print("Admin Access Granted.")
        return True
    else:
        print("Wrong Credentials! Access Denied.")
        return False
    
#User login...
# this function takes users username and password for Logging in of user Account for customer.
# the for loop iterates over the users and access each index of the list then the if statement targets user 
# directory looking for right key and its value for both username and password. 
# If true access granted. the else statement gives access denied as the credentials were entered wrong.
def private_user_login(username ,Password):
    for user in users:   #here for loop is used so that i can iterate overthe given list and add users and error does not occur. 
                         #If it was a dirctory direct if else would have worked.
        if user['user_name'] == username and user['password'] == Password:
            print("User Access Granted.")
            return True
        else:
            print("Wrong Credentials! Access Denied.")
            return False
        
# Guest users...       
def guest_user():
    return "Welcome, guest! You have accessed the application."

# Categories...
# the function lets us view product catalog in the store. It stores the asked products by a customer in a product list
# extracted from the database. Storage is done using append method.
def view_categories(category):
    print("Product Categories")
    product_list = []
    for product in categories[category]:  #Access products in a given category from categories.
        product_list.append(f"Product ID: {product['product_id']}, Name: {product['name']}, Category: {category}, Price: ₹ {product['price']}")
        return product_list
    
# the function adds category to the database. It uses category ids and increases a category using length method.
def add_category(category,products,user_type):
    if category not in categories:
        categories[category] = products
        category_ids[len(category_ids) + 1] = category
        print(f'Category {category} added Successfully.')
    else:
        print(f'Category {category} already Exists.')
    if user_type != admin:
            print("Error: Only Admin can Add Categories.")
            return

# the function removes a category from database. If-statement removes catagory from categories and the items method is used to
# iterate over the key values of category ids to remove the ids as well. 
def remove_category(category,user_type):
    if category in categories:
        del categories[category]
        for key, value in category_ids.items():
            del category_ids[key, value]
            print(f'Category {category} Removed Successfully.')
    else:
        print(f'Error: Category {category} not found.')
    if user_type != admin:
            print("Error: Only Admin can remove Categories.")
            return

# the function modifies components of categories. Only admin has rights to make these changes. It offers selecting of choices using 
# if-else statments. 1. New products added with prices using for loop and itrerate for products in it to add new product using length.
# append method includes new products. 1. Removing product using product id and remove method inside loop iteration of categories[category].
# 3. Using If-else category is renamed by deleting previous and assigning new name for category, also for loop iterates over category id
# key values are being matched. 4. Product is renamed through product id. for loop iterates over categories[category] for product as counter
# and name is replaced with new name given through input.
def modify_category(category,user_type):
    if category in categories:
        print("Category exists. What would you like to do?")
        print('1. Add a Product')
        print('2. Remove a Product')
        print('3. Rename a Category')
        print('4. Rename a Product')
        choice = input("Enter Your Choice:")
        if choice == '1':
            new_product = input("Enter the new Product: ")
            new_product_price = float(input("Enter the Product's Price: "))
            for product in categories[category]:
                product_id = len(categories[category]) + 1
                categories[category].append(f"Product ID: {product['product_id']}, Name: {product['name']}, Category: {category_ids[product['category_id']]}, Price: ₹ {product['price']}")
                print(f"Product {product_id}, {new_product} with {new_product_price} added successfully.")
        elif choice == '2':
            product_id = int(input("Enter the Product_ID to Remove the Product: "))
            for product in categories[category]:
                if product['product_id'] == product_id:
                    categories[category].remove(product)
                    print("Product removed Sucessfully.")
                else:
                    print("Product not found.")
        elif choice == '3':
            rename_category = input("Rename a Category: ")
            if rename_category in categories:
                print('Category already Exists!')
            else:
                del categories[category]
                categories[category] == categories[rename_category]
                for key, value in category_ids.items():
                    if value == category:
                        category_ids[key] = rename_category
                print(f"{rename_category} is the new category name.")
        elif choice == '4':
            product_id = int(input("Enter the Product_ID: "))
            for product in categories[category]:
                if product['product_id'] == product_id:
                    new_name = input("Enter the new name of the Product: ")
                    product['name'] == product[new_name]
                    print("Product renamed successfully.")
            else:
                print("Product not Found")
        else:
            print("Invalid choice.")
    else:
        print("Category doesnot Exist.")
    if user_type != admin:
            print("Error: Only Admin can Modify Categories.")
            return
            
#Cart Functions...

user_cart = {}

#creating a session_id per user
import math
import random

session_id = hex(random.randint(0, 2**100 - 1))[2:]
print(f"{session_id} is the Session_ID for {'username'}")

def view_cart(session_id,product,user_type):
    if session_id in user_cart:   # session_id is used to alot every user a perticular cart...
        for product , quantity in user_cart[session_id]:
            print (f"Product ID: {product['product_id']}, Name: {product['name']}, Quantity: {quantity}")
    else:
        print("Your cart is Empty")
    if user_type != users:
            print("Error: Only Users can Access Cart.")
            return

def add_to_cart(session_id,product_id,quantity,user_type):
    if session_id not in user_cart:   # if no cart ready...
        user_cart[session_id] = {}
    elif product_id in user_cart[session_id]:    # if any product already there...
        user_cart[session_id][product_id] += quantity
    else:
        user_cart[session_id][product_id] = quantity  # if there is no product in the cart...
        print("Item added to cart successfully.")
    if user_type != users:
            print("Error: Only Users can Access Cart.")
            return

def remove_from_cart(session_id,product_id,user_type):
    if session_id in user_cart and product_id in user_cart[session_id]:   # product removal if both conditions fulfilled
        del user_cart[session_id][product_id]
        print("Item removed from cart successfully.")
    else:
        print("Item not found in cart.")
    if user_type != users:
            print("Error: Only Users can Access Cart.")
            return
# payments...

def process_payment(username, amount, user_type):
        print("Please choose from the following Payment Methods: ")
        print('1. Unified Payment Interface')
        print('2. Debit Card/Credit Card')
        print('3. Net Banking')
        print('4. Cash On Delivery')
        choice = input("Enter Your Choice:")
        if choice == "1":
            print(f'Congratulations! {username}. You will be shortly redirected to the portal of Unified Payment Interface to make a payment of ₹{amount}')
        elif choice == "2":
            print(f'Congratulations! {username}. You will be shortly redirected to the portal of Debit Card/Credit Card to make a payment of ₹{amount}')
        elif choice == "3":
            print(f'Congratulations! {username}. You will be shortly redirected to the portal of Net Banking to make a payment of ₹{amount}')
        elif choice == "4":
            print(f'Congratulations! {username} on placing the order of ₹{amount}. Please pay your delivery executive. Thankyou!')
        else:
            print("Unsupported payment method.")
        if user_type != users:
            print("Error: Only Users can Access Payments.")
            return
        





