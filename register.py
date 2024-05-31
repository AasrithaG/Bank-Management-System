#User registration Signin Signup
from database import *
from customer import *
from bank import Bank
import random

def SignUp():
    username = input("Create Username: ")
    temp = db_query(f"SELECT username FROM customers WHERE username = '{username}';")
    if temp:
        print("Username Already Exists")
        SignUp()
    else:
        print("Username is Available Please Proceed")
        password = input("Enter your Password: ")
        name = input("Enter your Name: ")
        age = input("Enter your age: ")
        city = input("Enter your City: ")
        while True:
            account_number = int(random.randint(10000000, 99999999))
            temp = db_query(f"SELECT account_number FROM customers WHERE account_number = '{account_number}';")
            if temp:
                continue
            else:
                print(account_number)
                break
    cobj = Customer(username, password, name, age, city, account_number)
    cobj.createuser()
    bobj = Bank(username, account_number)
    bobj.create_transaction_table()
def SignIn():
    username = input("Enter Username: ")
    temp = db_query(f"SELECT username FROM customers WHERE username = '{username}';")
    if temp:
        while True:
            password = input(f"Welcome {username.capitalize()} Enter password: ")
            temp = db_query(f"SELECT password FROM customers WHERE username = '{username}';")
            if temp[0][0] == password:
                print("Sign In Successfully")
                return username
            else:
                print("Wrong password, Try Again")
                continue
    else:
        print("Enter Correct Username")
        SignIn()