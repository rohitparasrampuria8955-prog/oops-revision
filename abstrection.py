from abc import ABC,abstractmethod
# abstraction base class -> this is the only structure which will have important faunction
# abstract abse class -> is a class cannot be intstaniate directly and 
# serves as a bluprint for other calsses.
# it allows you to define a comman inteface a set of method and prpperties
# abstraction

# abstract class ->  A PRENT CLASS THAT CONTAAINTS ON OR MORE ABSTRACT METHOD
# abstract method -> a method that has a declaration bout no actual 
# implementation code.it focuse subclass to overright it

# concreate class: a normal subclass that provide real implimetation 
# for all the abstract method making it safe to in

class Vehical(ABC):

    # abstract class in which the abstract methos is defind but not the 
    # actual code is written for the basic implimataiton
    @abstractmethod
    def start(self):
        print("vehical start")
    @abstractmethod
    def stop(self):
        print("stop")

class Car(Vehical): # concerate class 
     def start(self):
        print("vehical start")

     def stop(self):
        print("stop")

obj= Car()


# decoratores 
# static method
# class method
