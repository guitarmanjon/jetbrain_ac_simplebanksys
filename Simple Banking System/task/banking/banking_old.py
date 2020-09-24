import random


class Account:
    def __init__(self, number, pin):
        self.number = number
        self.pin = pin
        self.balance = 0


def create_number():
    acc_no = "400000" + str(random.random() * 10000000000)[0:9] + str(random.randint(0, 9))
    # acc_no = str(random.random() * 10000000)[0:4]
    return acc_no


def create_pin():
    pin_no = str(random.random() * 10000000)[0:4]
    return pin_no


full_exit = False
accounts = []

while not full_exit:
    choice = int(input(" 1. Create an account \n 2. Log into account \n "
                       "0. Exit \n"))
    if choice == 1:
        temp_account = Account(create_number(), create_pin())
        accounts.append(temp_account)
        print("Your card has been created")
        print("Your card number:")
        print(temp_account.number)
        print("Your card PIN:")
        print(temp_account.pin)
    elif choice == 2:
        if len(accounts) == 0:
            print("No accounts!")
            continue
        correct_login = True
        print("Enter your card number:")
        user_acc = input()
        print("Enter your PIN:")
        user_pin = input()
        for acc in iter(accounts):
            if acc.number == user_acc and acc.pin == user_pin:
                partial_exit = False
                print("You have successfully logged in! \n ")
                while not partial_exit:
                    sub_choice = int(input(" 1. Balance \n 2. Log out \n "
                                           "0. Exit \n"))
                    if sub_choice == 1:
                        print("Balance: {}".format(acc.balance))
                    elif sub_choice == 2:
                        print("You have successfully logged out!")
                        partial_exit = True
                    elif sub_choice == 0:
                        print("Bye!")
                        partial_exit = True
                        full_exit = True
                    else:
                        print("Invalid choice. Please choose again.")
            else:
                correct_login = False
        if not correct_login:
            print("Wrong card number or pin!")
    elif choice == 0:
        full_exit = True
        print("Bye!")
    else:
        print("Invalid choice. Please choose again.")






