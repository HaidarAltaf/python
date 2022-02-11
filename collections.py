def temp(name):
    print(f"{name} is Temporary")

def eter(name):
    print(f"{name} is Eternal")

def RnT(name):
    print(f"{name} RIP AND TEAR")

    
    
    
    
    class Budget: # Creates template/blueprint that can be used by each object/category

    def __init__(self, name): # Pass name of category with the object

        self.name = name
        self.money = list()


    def deposit(self, amount): # Might need to pass other variables
        print(amount)
        print("Deposited")
        self.money.append(amount)

        # Write Code for deposit function




    def withdraw(self, amount): # Might need to pass other variables
        print(amount)
        print("Withdrawn")
        self.money.append(-amount)


        # Write Code for withdraw function



    def transfer(self, amount, account): # Might need to pass other variables
        print(amount)
        print("Transfered")
        if self.get_balance() > amount:
            self.withdraw(amount)
            account.deposit(amount)
            

            
        # Write Code for withdraw function



    def get_balance(self): # Might need to pass other variables
        bal_total = 0
        print("Balance")
        for x in self.money:
            bal_total += x
        return bal_total
        # Write Code for withdraw function





print("\nfood")
food = Budget("Food") # Creating an instance/object of the Budget class and passing in a name
food.deposit(4545)
food.withdraw(785)
print(food.get_balance())




print("\nclothes")
clothes = Budget("Clothes")
clothes.deposit(245)
clothes.withdraw(63)
clothes.transfer(7,food)
print(clothes.get_balance())



print("\nentertainment")
entertainment = Budget("Entertainment")
entertainment.deposit(3634)
entertainment.withdraw(5365)
entertainment.transfer(76, clothes)
print(entertainment.get_balance())
