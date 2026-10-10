class bank_account:
    def __init__(self, deposite, withdraw, balance):
        self.deposite = deposite
        self.withdraw = withdraw
        self.__balance = balance
    def Deposite(self, amount ):
        self.__balance+=amount
        print("Your account has balance ", self.__balance," after deposite")
    def With_Draw(self, amount):
        self.__balance-=amount
        print("Your account has balance ", self.__balance," after withdrawl")
    def Balance(self):
        print("Your account has current balance ", self.__balance,)




Ali = bank_account(6000,0,6000)
Ali.Deposite(5000)
Ali.With_Draw(2000)
Ali.Balance()
