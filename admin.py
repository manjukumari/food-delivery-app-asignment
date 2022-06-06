admin_keys = {'manju':'kumari'}

menu = { 1: {'foodname' : 'tandoori chicken', 'foodid' : 1, 'quantity' : 4, 'price' : 240, 'discount' : 40, 'stock' : 20},
         2: {'foodname' : 'vegan burger', 'foodid' : 2, 'quantity' : 1, 'price' : 320, 'discount' : 20, 'stock' : 20},
         3: {'foodname' : 'truffle cake', 'foodid' : 3, 'quantity' : 500, 'price' : 900, 'discount' : 20, 'stock' : 20},}

def add_new_food():
    foodname = input("Enter the Food Name :  ")
    foodid = int(input("Enter the Food Id :  "))
    quantity = int(input("Enter the Quantity :  "))
    price = int(input("Enter the price of the food: "))
    discount = int(input("Enter the discount :  "))
    stock = int(input("Enter the stock value of food : "))
    menu[foodid] = {
        "foodname" : foodname,
        "foodid" : foodid,
        "quantity" : quantity,
        "price" : price,
        "discount" : discount,
        "stock" : stock
    }
    print("\n The food "+foodname+" is successfully added \n")
    print ("updated menu is: ", menu)
    return menu


def edit_food_item():
    food = int(input("\n Enter the foodid which you want to edit :  "))
    name = input("Enter new food name :  ")
    amount = int(input("Enter the quantity :  "))
    cost = int(input("Enter the price of food :  "))
    off = int(input("Enter the discount :  "))
    stk = int(input("Enter the stock value of food :  "))
    menu[food]["foodname"] = name
    menu[food]["quantity"] = amount
    menu[food]["price"] = cost
    menu[food]["discount"] = off
    menu[food]["stock"] = stk
    print("\n ******* Edited Food Id Successfully!!!******* \n")
    print(menu)
    return menu

def price_cal(foodid):
    foodid = int(input("Enter foodid: "))
    a= menu[foodid]['price']
    b= menu[foodid]['discount']
    price = a-(a*b/100)
    return price



def view_menu():
    print("\n ******* Here is the MENU of FOOD DELIVERY APP *******")
    print("_______________________________________________________")

    def pieces(i):
        print("Food ID : ", menu[i]["foodid"],end = "  ")
        print("Food Name: ", menu[i]["foodname"],end = "  ")
        print("Quantity : ", menu[i]["quantity"],"pieces",end = "  ")
        print("price : ", menu[i]["price"],"INR", end = "  ")
        print("discount : ", menu[i]["discount"],"%",end = "  ")
        print("Stock :  ", menu[i]["stock"])

    pieces(1)
    pieces(2)
    def pieces(i):
        print("Food ID : ", menu[i]["foodid"],end = "  ")
        print("Food Name: ", menu[i]["foodname"],end = "  ")
        print("Quantity : ", menu[i]["quantity"],"gm",end = "  ")
        print("price : ", menu[i]["price"],"INR", end = "  ")
        print("discount : ", menu[i]["discount"],"%",end = "  ")
        print("Stock :  ", menu[i]["stock"])

    pieces(3)
    return menu

def remove_food_item():
    id = int(input("\n Enter the Food ID which you want to remove :  "))
    menu.pop(id)
    print("\n Food Item removed successfully")
    print(menu)
    return menu
        
    
                      
