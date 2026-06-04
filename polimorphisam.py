# polymorphism -> polymorphism is a fundamental concept in object-oriented programing
# that allow differant object to respond to the same function call or method in there owen way.
# poly => many
# morphism => forms

# type of ploymorphysm 
# 1. runtime polymorphisam ya method overrinding
# 2 . commpile time polemorphisam 

# method overloading -> method overloading  ia a core objext orinented programming concept that allows a class to 
# have multipal method 

# why python does not support overloading
        # pyhton does not support tradition method overloading primaerily because it is a dymamicall tpyed language that manages method 
# name witgin a dictionary-based namspace

#  method overloading can be achived by using the default argument
# or we canachive the method overloading by using variable length arguments

def add (*arrgs):
    return sum(arrgs)

print(add(12,3,45,7))

# method overriding -> method overriding in pyhton occures when a child class (subclass)
 #provides ita own implementation of a method that is already defined in its prentclass (superclass
 
 
 


class Vehical:
    def start(self):
        print("the vehical starts")

class Car(Vehical):
    def start(self):
        return('the car starts with keys')

car = Car()
print(car.start())


class DeliverySystem:
    def deliver(self):
        print("this platfrom deliver somthing")

class Zomato(DeliverySystem):
    def deliver(self):
        print("zomato deliver food")

class Instamart(DeliverySystem):
    def deliver(self):
        print("instamart deliver grocery")

platforms = [Zomato(),Instamart()]
for platform in platforms:
    platform.deliver()


# interview question base on the inheritance polymorphisam , encapsulation






