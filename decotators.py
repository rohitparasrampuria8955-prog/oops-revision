def login(func):
    def bind():
        print('please login hear')
        func() # show profile
        print ('logged out')
    return bind # show profile

@ login
def show_profile():
    print("here is your photo")

show_profile()


# class method

class student:
    university = 'IIT'

    def __init__(self,name,age):
        self.name = name
        self.age = age
    @classmethod
    def change_name(cls,new_name):
        cls.university = new_name

obj = student('vinay',24)
obj.change_name('IIT Kanpur')
print(obj.university)






class student:
    university = 'IIT'

    def __init__(self,name,age):
        self.name = name
        self.age = age
    @classmethod
    def change_name(cls,new_name):
        cls.university = new_name

    @staticmethod
    def calculate_percentage():
        return "this will return some percentage"

obj = student('vinay',24)
obj.change_name('IIT Kanpur')
print(obj.university)

student.university
