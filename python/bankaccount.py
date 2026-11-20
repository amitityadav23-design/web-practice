class bankaccount:
    def __init__(self,balance):
        self.__balance=balance
    def show_balance(self):
        print(self.__balance)
s1=bankaccount(500)
s1.show_balance() 