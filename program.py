import random
def login():
    print("Please enter your details to log in")
    x=True
    while x==True:
        username1 = str(input("Please enter your username: "))
        password1 = str(input("Please enter your password: "))

        file = open("staff.txt", "r")
        for row in file:
            field = row.split(",")
            username = str(field[0])
            password = str(field[1])

            if username1 == username and password1 == password:
                print("Hello", username)
                x=False
                break
        else:
            print("incorrect")
            print("try again")

def functions():
    while True:
        try:
            print('Enter 1 to Create New Bank Account')
            print('Enter 2 to Check Account Details')
            print('Enter 3 to logout')
            num2 = int(input(">>>> "))
            if num2==1:
                print("Fill the Form Below: ")
                acc_name=input(str("Account Name>>> "))
                amount=str(input("Opening Balance>>> "))
                acc_type=input(str("Account Type>>> "))
                acc_mail=input(str("Account Email>>> "))
                acc_num=str(random.randint(1000000000,1999999999))
                print(f"The Account number for {acc_name} is {acc_num}")
                file = open("customer.txt", "a")
                file.write(acc_name)
                file.write(",")
                file.write(amount)
                file.write(",")
                file.write(acc_type)
                file.write(",")
                file.write(acc_mail)
                file.write(",")
                file.write(acc_num)
                file.write("\n")
                file.close()
                print("Your details have been saved. ")
            if num2==2:
                while True:
                    try:
                        print("Enter Account Number: ")
                        accountnum=str(input(">>>> "))
                        file = open("customer.txt", "r")
                        for row in file:
                            field = row.split(",")
                            acc_name = str(field[0])
                            amount = str(field[1])
                            acc_type = str(field[2])
                            acc_mail = str(field[3])
                            acc_num = str(field[4])
                            lastchar = len(acc_num) - 1
                            acc_num = acc_num[0:lastchar]
                            if str(accountnum) == acc_num:
                                print(f"Account Name- {acc_name}")
                                print(f"Opening Balance- {amount}")
                                print(f"Account Type-{acc_type}")
                                print(f"Account Email-{acc_mail}")
                                file.close()
                                break
                        else:
                            print("Invalid Account Number")
                        break
                    except ValueError:
                        print("Account Number must be Integers: ")
                    except IndexError:
                        print()
            if num2==3:
                break
        except ValueError:
            print("Invalid Input")

def program():
    while True:
        try:
            print("Enter 1 for Staff login: ")
            print("Enter 2 for Close App: ")
            num=int(input(">>>> "))
            if num==1:
                login()
                functions()
            else:
                break
        except ValueError:
            print("Invalid Input")


program()