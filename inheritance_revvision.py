#  inheritance is the one of the most important pillar of opps in which inherit
# proparties of the parent class is to passed to child class

class Dad: # parant calss or base classs
    prop = 'highway wali jameen!'

class Child(Dad): # Child class oe drived class
    pass

ram = Child()
ram.prop


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


# multipal or multilavel inheritance
# what is the differance between mutipal or multilavel inheritance
"""multipal inheritance occure when a singal class inherits getaure from two or more parent classes
multilavel inheritance forms a chain where a class inherits from a derived class making that parent both a child and parent

1.>= base class ->1 child class in multiple inheritance
1 class a -> class b -> class c"""
# 

# multilavel inheritance =>

# c


# multipal inheritance
class Mother:
    management_skills='home management skilles'
    def __init__(self,name):
        self.mother_name=name

class Father:
    finance_skill = 'Financial Skilles'
    def __init__(self,name):
        self.father_name=name
class Child(Mother,Father):
    sports_skills='Sports_skills'
    def __init__(self,student_name,father_name,mother_name,):
        Mother.__init__(self,mother_name)
        Father.__init__(self,father_name)
        self.student_name = student_name

    def display(self):
        print(f'Studnet name :{self.student_name}')
        print(f"father name :{self.father_name}")
        print(f"mother name :{self.mother_name}")
obj = Child("rohit","sanjay",'santosh')
obj.display()


# what is methos resoulation order ya mro -> in the sequence in which pyhton sacrchs for a method or attribute
# in a class hierarchy it is essenital for resolving which method to enxcute when ultipoal class in an inheritance chain
# define a method with the same name,a common occurrence in multipale inheritance