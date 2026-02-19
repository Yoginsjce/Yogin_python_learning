class BankAccount:
    def __init__(self, acc_no,balance):
        self.__acc_no=acc_no
        self.__balance=balance
        

    def show_balance(self):
        print(f"the remaining balance in acc is {self.__balance}")

    def withdraw(self,amount):
       if amount > self.__balance:
           print("Insufficeint funds")
           return
       print(f"Amount sucessfully withdrawn")
       self.__balance-=amount
       print(f"after withdraw balance is {self.__balance}")

    def deposit(self,amount):
        print("Amount deposited Succesfully")
        self.__balance+=amount
        print(f"After deposit balance is {self.__balance}")

B1=BankAccount(4756,10000)
B2=BankAccount(9785,89000)

B1.show_balance()
B1.deposit(1200)
B1.withdraw(90)