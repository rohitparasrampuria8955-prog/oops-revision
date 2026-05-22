#  inheritance is the one of the most important pillar of opps in which inherit
# proparties of the parent class is to passed to child class

# class Dad: # parant calss or base classs
#     prop = 'highway wali jameen!'

# class Child(Dad): # Child class oe drived class
#     pass

# ram = Child()
# ram.prop


class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        for key,value in self.__dict__.items():
            print(f'{key}:{value}')
class Doctor(Human):
    def __init__(self,name,age,sp): # automatically call
        super().__init__(name,age) # parent class manually
        self.sp = sp # adding the new property of hte humna + sp doctor
class Teachar(Human):
    def __init__(self,name,age,sub):
        super().__init__(name,age)
        self.sub=sub
class Engineer(Human):
    def __init__(self,name,age,stream):
        super().__init__(name,age)
        self.stream=stream
obj = Doctor('Dr_Gulati',35,'Dentis')
obj.display()

obj = Teachar("vinay_sir",24,'Pyhton')
obj.display()