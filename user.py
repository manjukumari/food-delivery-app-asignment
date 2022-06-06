import admin as ad

class User:
    username = " "
    password = " "
    login_info = {"username":username, "password": password}

    def __init__(self, name, number, email, address, password):
        self.name = name
        self.number = number
        self.email = email
        self.address = address
        self.password = password
        User.login_info["username"] = name
        User.login_info["password"] = password
        self.profile={"Name":name}
        self.order_history = {}

    @classmethod
    def login(cls,name,password):
          if cls.login_info["username"]== name and cls.login_info["password"] == password :
            print("You're are successfully logged in!!!!")
            return True
          else:
            print("SORRY! These are the Wrong Credentials!")
            return False

    def place_order(self):
        print("\n What you want to order here in the Menu? \n")
        print(ad.view_menu())
        user_choice = int(input("\n If you want to order then select \n 1.YES \n 2.NO \n "))
        if user_choice == 1:
            n=int(input("\n Enter how many food items do you want to Order? \n"))
            x=0
            for i in range(n):
             foodid = int(input("\n Enter the food id here: "))
             quan = int(input("\n Enter the quantity of the food : "))
             quantity =int(ad.menu[foodid]['quantity'])
             price = ad.price_cal(foodid)
             print("total price for this item is: ",price)
             
             if quan<= quantity:
              x = x + ((price * quan)/quantity)
              print("your bill is: ",x)
             else:
                 print("\n oops the minimum order has already been given :( \n")
             if x>1000:
                 x = x- ((x*10)/100) 
             again_ask = input("\n Your order is ready!! Do you want to order this? \n Enter YES or NO: \n")
             if again_ask == "YES":
                print(f'''\n Your food name is {ad.menu[foodid]['foodname']}''')
                print(f'''\n Price of your food is {ad.menu[foodid]['price']}''')
                print(f"\n This is your quantity {quan}")
                print(f"\n It costs you {x}INR in total")
                print("\n You're all set for this order")
                self.order_history[foodid] = {
                    'foodname': ad.menu[foodid]['foodname'],
                    'price': ad.menu[foodid]['price'],
                    'quantity': quan
                }
                final_stock = ad.menu[foodid]['stock'] - quan
                ad.menu[foodid]['stock'] = final_stock
                
                print("\n You're order is successfully placed! \n ")

             elif again_ask == "NO":
                print("\n This Order is cancelled!! You can look once more! \n")
            else:
                print("\n Invalid choice!")
        elif user_choice == 2:
            print("\n You select 2 option so we cancelled this! \n")
        else:
            print("\n Entered the invalid choice! \n")
            
    def display(self):
        print("please enter name:",self.name)
        print("eneter number:",self.number)
        print("enter email:",self.email)
        print("enter adress:",self.address)
        print("please enter password:",self.password)
        print("enter your login_info:",User.login_info)
        
    def account_register():
      cs = User(input("name: "),int(input("enter phone_no: ")),input("email_id: "),input("enter_ adress: "),input("enter password: "))
      return cs.display()



    def account_update():
      cs = User(input("name: "),int(input("enter phone_no:  ")),input("email_id: "),input("enter_ adress: "),input("enter password: "))
      return cs.display()
