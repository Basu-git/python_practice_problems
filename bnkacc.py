# " Create a `BankAccount` class with private attributes for `account_number` and `balance`.- Add methods to check balance, deposit, and withdraw funds.- Try accessing the balance directly and observe the result."
class bankaccount:
    def __init__(self,acc_no,balance):
        self.__acc_no=acc_no
        self.__balance=balance
    def balance(self):
        print(f"The initial balance {self.__balance}")
    def dep(self,amt):
        if amt>0:
            self.__balance+=amt
            print(f"The balance is {self.__balance}")
        else:
            print("Deposit amt must be in positive numbers Negative numbers are not allowed")
    
    def withdraw(self,amt):
        if amt>0:
            self.__balance-=amt
            print(f"The balance of cuureent acc is {self.__balance}")
        else:
            print("Withdraw  amt must be in positive numbers Negative numbers are not allowed")
a=bankaccount(65029213757,1000)
a.balance()
a.dep(100)
a.withdraw(-1)