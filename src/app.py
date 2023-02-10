import menu_options as menu
import model

def navigate_main_menu():
    while True:
        print(menu.main)
        try:
            cmd = int(input("Please enter your response here -> "))
        except ValueError:
            print("Error: Please enter a number.")
        if cmd == 0:
            exit()
        elif cmd == 1:
            navigate_product_menu()
        elif cmd == 2:
            navigate_courier_menu()
        elif cmd == 3:
            navigate_order_menu()
        else:
            print("Please enter a number between 0 and 4")

def navigate_product_menu():
        while True:
            print(menu.products)
            try:
                cmd = int(input("Please enter your response here -> "))
            except ValueError:
                print("Error: Please enter a number.")
            if cmd == 0:
                navigate_main_menu()
            elif cmd == 1:
                model.print()
            elif cmd == 2:
                model.add()
            elif cmd == 3:
                model.update()
            elif cmd == 4:
                model.delete()
            else:
                print("Please enter a number between 0 and 4")




def navigate_courier_menu():
    while True:
            print(menu.couriers)
            try:
                cmd = int(input("Please enter your response here -> "))
            except ValueError:
                print("Error: Please enter a number.")
            if cmd == 0:
                navigate_main_menu()
            elif cmd == 1:
                model.print_couriers()
            elif cmd == 2:
                model.add()
            elif cmd == 3:
                model.update()
            elif cmd == 4:
                model.delete()
            else:
                print("Please enter a number between 0 and 4")




def navigate_order_menu():
    while True:
            print(menu.orders)
            try:
                cmd = int(input("Please enter your response here -> "))
            except ValueError:
                print("Error: Please enter a number.")
            if cmd == 0:
                navigate_main_menu()
            elif cmd == 1:
                model.print()
            elif cmd == 2:
                model.add()
            elif cmd == 3:
                model.update_status()
            elif cmd == 4:
                model.update_order()
            elif cmd == 5:
                model.delete()
            else:
                print("Please enter a number between 0 and 4")




def main():
    if __name__ == "__main__":
        navigate_main_menu()



main()