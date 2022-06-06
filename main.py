import admin as aa
import user as us
from user import User


uhh = User(str, str, str, str, str)

inp = int(input("\n Where do You want to login? \n select: \n 1.Admin \n 2.User \n 3.Exit \n "))
if inp == 1:
    
    Username = input("Enter the username of admin: ")
    Password = input("Enter the password of admin: ")
    if aa.admin_keys[Username] == Password:
        print("\n *****You're successfully logged in!*****")
        admin_crawler = True
        while admin_crawler:
            adm_choice = int(input("\n Choose the options of admin panel: \n 1.ADD NEW FOOD ITEM \n 2.EDIT FOOD ITEM \n 3.VIEW MENU \n 4.REMOVE FOOD ITEM \n 5.EXIT \n "))
            if adm_choice == 1:
                aa.add_new_food()
            elif adm_choice == 2:
                aa.edit_food_item()
            elif adm_choice == 3:
                aa.view_menu()
            elif adm_choice == 4:
                aa.remove_food_item()
            elif adm_choice == 5:
                print(f"\n You're Exit from the admin panel {Username}! ")
                admin_crawler = False
            else:
                print("\n This is the wrong selection please select valid option ")
    else:
        print("\n These are the wrong credentials! SORRY!!! ")
elif inp == 2:
    print("Welcome to the user panel, resister your account")
    User.account_register()
    username = input("Enter the username here: ")
    password = input("Enter the password here: ")
    if User.login(username, password):
     print(f"You are logged in successfully {username}!!")
    user_crawler = True
    while user_crawler:
            usr_choice = int(input(f"\n {username}, Enter the option: \n 1.Place new order \n 2.Order history \n 3.update profile \n 4.Exit  "))
            if usr_choice == 1:
                uhh.place_order()
            elif usr_choice == 2:
                print(f"\n Here is your order history, {username}: \n ")
                print(uhh.order_history)
            elif usr_choice == 3:
                print(User.account_update())
                print(f"\n your profile is updated, {username}! \n ")
            
            elif usr_choice == 4:
                user_crawler = False
                print("\n You're Successfully logged out!\n ")
            else:
              print("\n You choose the invalid option! \n")
    else:
      print("sorry you've entered wrong credentials!!")
else:
    exit()



