#create Account with 2 attribute -balance & account no 
# crete method for debite,credite & printing the balance 
class account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account=acc


        #debit method 
    def debit(self,amount):
        self.balance -=amount
        print("RS." ,amount,"was debite")
        print("total balance",self.get_balance())
        #credite method 
    def credit(self,amount):
        self.balance +=amount
        print("RS." ,amount,"was credited")
        print("total balance",self.get_balance())

    def get_balance(self):
        return self.balance

acc1=account(1000,1234)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(45000)