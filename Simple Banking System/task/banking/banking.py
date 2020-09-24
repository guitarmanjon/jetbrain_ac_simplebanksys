import random
import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()

# create table
cur.execute('CREATE TABLE IF NOT EXISTS card ('
            'id INTEGER,'
            'number TEXT,'
            'pin TEXT,'
            'balance INTEGER DEFAULT 0)'
            )
conn.commit()


def gen_can():
    # return str(random.randint(10, 99)) # for debugging
    return str(random.randint(10000000, 99999999))


def gen_checksum(input_card_no):
    total_list = list(input_card_no)
    total_list_int = []
    for x in total_list:
        total_list_int.append(int(x))
    for y in range(len(total_list_int)):
        if y % 2 == 0:
            temp_int = total_list_int[y]
            total_list_int[y] = temp_int * 2 if temp_int * 2 <= 9 \
                else temp_int * 2 - 9
    total = sum(total_list_int)
    return 0 if total % 10 == 0 else 10 - (total % 10)


def check_checksum(card_num: str):
    # use the input card number to generate a checksum
    # compare generate checksum against that passed in with
    new_check_sum = str(gen_checksum(card_num[0:len(card_num) - 1]))
    # print(new_check_sum + "     old: " + card_num[len(card_num)-1])
    return card_num[len(card_num)-1] == new_check_sum


def gen_pin():
    return str(random.randint(1000, 9999))


def new_account(iin, can):
    return iin + can + str(gen_checksum(iin + can))


accounts = dict()

full_exit = False

while not full_exit:
    choice = int(input(" 1. Create an account \n 2. Log into account \n "
                       "0. Exit \n"))
    if choice == 1:
        new_acc_no = new_account("4000000", gen_can())
        # new_acc_no = new_account("40", gen_can()) # for debugging
        new_pin = gen_pin()
        accounts[new_acc_no] = new_pin
        print("Your card has been created")
        print("Your card number:")
        print(new_acc_no)
        print("Your card PIN:")
        print(new_pin)
        cur.execute('INSERT INTO card'
                    '   (number, pin, balance)'
                    '   VALUES ({}, {}, {})'.format(new_acc_no, new_pin, 0))
        conn.commit()
    elif choice == 2:
        print("Enter your card number:")
        user_acc = input()
        print("Enter your PIN:")
        user_pin = input()
        if user_acc in accounts:
            if accounts[user_acc] == user_pin:
                partial_exit = False
                print("You have successfully logged in! \n ")
                while not partial_exit:
                    cur.execute('SELECT * FROM card WHERE number = {}'
                                .format(user_acc))
                    curr_user = cur.fetchall()
                    sub_choice = int(input(" 1. Balance \n 2. Add income \n "
                                           "3. Do transfer \n 4. Close account \n"
                                           " 5. Log out \n 0. Exit \n"))
                    if sub_choice == 1:
                        print("Balance: {}".format(curr_user[0][3]))
                    elif sub_choice == 2:
                        income = int(input("Enter income: "))
                        cur.execute('UPDATE card SET balance = balance + {inc} WHERE number = {num};'
                                    .format(inc=income, num=user_acc))
                        conn.commit()
                        print("Income was added!")
                    elif sub_choice == 3:
                        print("Transfer \nEnter card number:")
                        trans_to = input()
                        #   Check account to transfer to exists
                        cur = conn.execute('SELECT EXISTS ( SELECT * FROM card WHERE number = {});'
                                           .format(trans_to))
                        exists = cur.fetchall()
                        if trans_to == user_acc:
                            print("You can't transfer money to the same account!")
                        elif not check_checksum(trans_to):
                            print("Probably you made a mistake in the card number. Please try again!")
                        elif not exists[0][0]:
                            print('Such a card does not exist.')
                        else:
                            print('Enter how much money you want to transfer:')
                            tx_amount = int(input())
                            if curr_user[0][3] < tx_amount:
                                print("Not enough money!")
                            else:
                                # reduce curr_user balance by tx_amount
                                conn.execute('UPDATE card SET balance = balance - {} WHERE number = {}'
                                             .format(tx_amount, user_acc))
                                conn.commit()
                                # add tx_amount to trans_to
                                conn.execute('UPDATE card SET balance = balance + {} WHERE number = {}'
                                             .format(tx_amount, trans_to))
                                conn.commit()
                                print("Success!")
                    elif sub_choice == 4:
                        conn.execute('DELETE FROM card WHERE number = {}'
                                     .format(user_acc))
                        conn.commit()
                        print("The account has been closed!")
                    elif sub_choice == 5:
                        print("You have successfully logged out!")
                        partial_exit = True
                    elif sub_choice == 0:
                        print("Bye!")
                        partial_exit = True
                        full_exit = True
                    else:
                        print("Invalid choice. Please choose again.")
            else:
                print("Wrong card number or PIN!")
        elif user_acc not in accounts:
            print("Wrong card number or PIN!")
    elif choice == 0:
        full_exit = True
        print("Bye!")
    else:
        print("Invalid choice. Please choose again.")
