import random
from datetime import datetime
import time
class Bank:
    __account_types = {"fixed" : "Fixed Account", "savings" : "Savings Account" }
    __Bank_name="Biraj Bank"
    __interest_rate_Savings=6.05
    __interest_rate_Fixed=11.55
    def __init__(self, fn,ln,addr,age,type, password, balance, Account_number,accrued_interest):
        self.__fn=fn
        self.__ln=ln
        self.__addr=addr
        self.__age=age
        self.__type=type
        self.__balance=balance
        self.__password=password
        self.__accrued_interest=accrued_interest
    

    @staticmethod         
    def Account_first():
        print("\n You do not have any Account yet. \nPlease create an Account first. ")  
    

    @staticmethod            
    def print_bank_holidays():
        print(f"\nBaishakh 4, 11, 18, 25 \nJestha 1, 8, 15, 22, 29 \nAshadh 5, 12, 19, 26 \nSharwan 2, 9, 16, 23, 30 \nBhadra 5, 12, 19, 26 \nAshoj 2, 9, 16, 23, 30 \nKartik 6, 13, 20, 27 \nMangsir 4, 11, 18, 25 \nPoush 3, 10, 17, 24 \nMagh 1, 8, 15, 22, 29 \nFalgun 7, 14, 21, 28 \nChaitra 5, 12, 19, 26")


    @classmethod
    def get_interest_rate(cls):
        interest_rate = cls.__interest_rate_Savings if cls.__type == Bank.__account_types['savings'] else cls.__interest_rate_Fixed
        print(f"\nSince you have {cls.__type}, your interest rate is {interest_rate} \n Note** Interest is accrued every 5 mins.")
       

    @classmethod
    def get_account_type(cls, type):
        return Bank.__account_types[type]
    

    @classmethod
    def get_school_name(cls):
        return Bank.__Bank_name


    def display_Account_details(self):
        print(f"\nACCOUNT HOLDER : {self.__fn.upper()} {self.__ln.upper()} \nADDRESS : {self.__addr.upper()} \nAGE : {self.__age} \nACCOUNT TYPE : {self.__type.upper()} \nACCOUNT CURRENT BALANCE : {self.__balance} \nPASSWORD : {self.__password} \nAccrued Interest : {self.__accrued_interest}")

    
    def verify_password(self):
        global verification
        verification=input("Enter your password to proceed. ")
        
        if verification !=  self.__password:
            print("\nYour Password is wrong. ")
        else:
            pass


    def get_current_balance(self):
        print(f"\nYour Current Balance Amount is : {self.__balance}. ") 


    def deposit_money(self, deposit_amount):
        if deposit_amount<0:
            print("\nPlease enter a valid amount. ")

        else:
            self.__balance += deposit_amount
            print(f"\nYour Updated amount is {self.__balance} ")


    def withdraw_money(self, withdraw_amount):
        if withdraw_amount<0:
            print("\nPlease enter a valid amount. ")

        elif withdraw_amount >self.__balance:
            print(f"\nInsufficient balance. You can only withdraw upto {self.__balance}")

        else:
            self.__balance -= withdraw_amount
            print(f"\nYour Updated amount is {self.__balance} ")


    def change_account_type(self):

        if self.__type ==Bank.__account_types["savings"]:
            type_choice=input(f"You have {self.__type} as of now. Do you want to change it to Fixed Account? \n Press Y for Yes and N for No. ")

            if type_choice=="Y":
                self.__type = Bank.__account_types["fixed"]
                print(f"You have changed your account type to {self.__type}")

            else:
                print(f'Your account type remains unchanged.')

        elif self.__type ==Bank.__account_types["fixed"]:
            type_choice=input(f"\nYou have {self.__type} as of now. Do you want to change it to Savings Account? \n Press Y for Yes and N for No. ")

            if type_choice=="Y":
                self.__type =Bank.__account_types["savings"]
                print(f"You have changed your account type to {self.__type}")

            else:
                print(f'Your account type remains unchanged.')


    def change_password(self):
        old_password=input("Enter your old password again.")

        if old_password != self.__password:
            print("Your old password is incorrect. \n Try Again.")

        elif old_password == self.__password:
            new_password=input("Enter your new password.")
            self.__password=new_password


    def get_password(self):
        return self.__password


    def check_accrued_interest(self):

        if self.__type==Bank.__account_types["savings"]:
            self.__accrued_interest=self.__balance*(6.05/100)
            return self.__accrued_interest

        elif self.__type==Bank.__account_types["fixed"]:
            self.__accrued_interest=self.__balance*(6.05/100)
            return self.__accrued_interest


    def transfer_interest(self):
        choice=input("Do you want to transfer all your accrued interest to youe main account? \n Press Y for Yes and N for No.")

        if choice=="N":
            print('Your accrued interest is not transferred to your main account.')

        if choice=="Y":
            self.__balance+=self.__accrued_interest
            self.__accrued_interest=0

    
user = None
while True:

    print(f'\n Welcome to {Bank.get_school_name()} \n Today is {datetime.now()}')
    
    user_choice=input("\n Press 1 to create an acoount. \n Press 2 to check current balance. \n Press 3 to deposit money in the bank. \n Press 4 to withdraw money from the bank. \n Press 5 to check your account interest rate. \n Press 6 to change account type. \n Press 7 to display holidays of the bank. \n Press 8 to delete your account. \n Press 9 to check your Bank details. \n Press 10 to change password. \n Press 11 to check ACCRUED interest. \n Press 12 to tranfer accrued interest. ")

#Choice 1
    if user_choice == "1" and user==None:
        user_fn=input("Enter your first name. ")
        user_ln=input("Enter your last name. ")
        user_addr=input("Enter your Address. ")
        user_age=int(input("Enter your age. "))
        user_type=input(f"Which Bank Account type do you like to open? \n Press 1 for Savings Account. Press 2 for Fixed Account. ")
        if user_type == "1":
            user_type=Bank.get_account_type('savings')

        if user_type == "2":
            user_type = Bank.get_account_type('fixed')

        user_password=input("Create a password to access other features. ")
        user_balance=input("Do you want to initially deposit some money? \n Press Y for yes and N for No. ")
        if user_balance=="Y":
            user_balance=int(input("Enter an amount that you want to deposit initiialy. "))

        elif user_balance=="N":
            user_balance=0

        user_Account_number=random.randint(10000000,100000000)
        user_accrued_interest=0
        user= Bank(user_fn,user_ln, user_addr, user_age, user_type, user_password, user_balance,user_Account_number,user_accrued_interest)

        print(f"\nCongratulations. You have created your Account. You can view your details by pressing 9. Your Account number is {user_Account_number} ")

    elif user_choice == "1" and user is not None:
        print(f"\n You already have an account named {user_fn} {user_ln}. \n Please delete your current Account by pressing 8 before creating a new account.")

#Choice 2
    elif user_choice =="2" and user is None:
        Bank.Account_first()

    elif  user_choice =="2" and user is not None:
        user.verify_password()

        if verification==user.get_password():
           user.get_current_balance()

#Choice 3
    elif user_choice=="3" and user is None:
        Bank.Account_first()

    elif user_choice=="3" and user is not None:
        user.verify_password()
        
        if verification==user.get_password():
            deposit_amount=int(input("Enter deposit amount."))
            user.deposit_money(deposit_amount)
    
#Choice 4    
    elif user_choice=="4" and user is None:
        Bank.Account_first()

    elif user_choice=="4" and user is not None:
        user.verify_password()
        
        if verification==user.get_password():
            withdraw_amount=int(input("Enter withdraw amount."))
            user.withdraw_money(withdraw_amount)

#Choice 5
    elif user_choice=="5" and user is None:
        Bank.Account_first()

    elif user_choice=="5" and user is not None:
        user.verify_password()

        if verification==user.get_password():
            user.get_interest_rate()

#Choice 6
    elif user_choice=="6" and user is None:
        Bank.Account_first()

    elif user_choice=="6" and user is not None:
        user.verify_password()

        if verification==user.get_password():
            user.change_account_type()

#Choice 7
    elif user_choice=="7":
        Bank.print_bank_holidays()

#Choice 8
    elif user_choice=="8" and user is None:
        Bank.Account_first()
      

    elif user_choice=="8" and user is not None:
        user.verify_password()

        if verification==user.get_password():
            print(f"\nYour account named {user_fn} {user_ln} has been deleted. \n In case you like to create a new Account, please press 1.")
            user=None

#Choice 9
    elif user_choice=="9" and user is None:
        Bank.Account_first()

    elif user_choice=="9" and user is not None:
        user.verify_password()

        if verification==user.get_password():
            user.display_Account_details()

#choice 10
    elif user_choice=="10" and user is None:
        Bank.Account_first()

    elif user_choice=="10" and user is not None:
        user.verify_password()

        if verification==user.get_password():
            user.change_password()

#choice 11
    elif user_choice=="11" and user is None:
        Bank.Account_first()

    elif user_choice=="11" and user is not None:
        user.verify_password()

        if verification==user.get_password():
            print(user.check_accrued_interest())

#choice 12
    elif user_choice=="12" and user is None:
            Bank.Account_first()

    elif user_choice=="12" and user is not None:
        user.verify_password()

        if verification==user.get_password():
            user.transfer_interest()
            
#Wrong Choice    
    else:
        print("Enter a valid Code from 1 to 12")
