# encapusulation -> encapsulation is one of most important pillar of oops 
# in which we bind the data into one unit.. so,that the access on the 
# attributes should be restricted

# type of atribute in oops
# public atribute -> accessibal from everyehere the defailt in pyhton
# private atribute -> suggest to membet os internal and should only be used within the class and its subclass
# protected attribute -> trigar name mangling making is harder (but not impossibal )
# to accesss from outside from outside the class.

# what is a name mangling -> name mangling is the way to access a privet 
# atribute out side of class

# name mangling is a machanisam that prevent accidental name conflict between attribute
# of a class and its sub calss it is often mistake for a way to create privet variable but is primary
# purpose it to insure that internal

class Bank_Account:
    def __init__(self,name,amount,pin):
        self.name=name  # public atribute
        self._amount = amount # protected attribute
        self.__pin = pin # privet attribute
# wha is satter
# satter is a method through which we set the new vlaues of privat & protectes attrinute
    def change_pin(self,new_pin):
        self.__pin = new_pin
        print("pin change sucessfully")

# gater is method through which we get the privet and protected attributes        
    def chaek_balance(self):
        print(f'current balance : {self.chaek_balance}')

# inpliment a method to deposite the amount into account
# impliment a method through which withdraw the money
# first of all you have check the pin 
# the amount which have to be withdraen that shuldnt be more then balance

    def deposite(self,deposit_amount):
        self._amount += deposit_amount
        print(f'{deposit_amount} is successfully deposited')
    
    def withdraw(self,pin):
        if self.pin == self.__pin:
            withdraw_amount = int(input("Enter your amount"))
            if withdrw_amount <= self._amount:
                withdrw_amount -= self._amount
            else:
                print("insuficeint balance")




acc=Bank_Account('ram',3000,1234)
# print(acc._amount)
# print(acc._Bank_Account__pin)
