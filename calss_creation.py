# 1. Create a Student Class

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_student(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student("Vinay", 22)

s1.display_student()

# 2. Create a Car Class

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_car(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

c1 = Car("Toyota", "Fortuner")
c2 = Car("Hyundai", "Creta")

c1.display_car()
print()

c2.display_car()

# 3. Create a Book Class

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_book(self):
        print("Title:", self.title)
        print("Author:", self.author)
b1 = Book("Python Basics", "Rohit Sharma")

b1.display_book()

# 4. Create a Mobile Class

class Mobile:
    def __init__(self, company, price, ram):
        self.company = company
        self.price = price
        self.ram = ram

    def display_mobile(self):
        print("Company:", self.company)
        print("Price:", self.price)
        print("RAM:", self.ram)
m1 = Mobile("Samsung", 30000, "8GB")

m1.display_mobile()

# 5. Create a Laptop Class

class Laptop:
    def __init__(self, brand, processor, price):
        self.brand = brand
        self.processor = processor
        self.price = price

    def display_laptop(self):
        print("Brand:", self.brand)
        print("Processor:", self.processor)
        print("Price:", self.price)
l1 = Laptop("HP", "Intel i5", 55000)

l1.display_laptop()

# 6. Create a Dog Class

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def display_dog(self):
        print("Name:", self.name)
        print("Breed:", self.breed)
d1 = Dog("Tommy", "Labrador")

d1.display_dog()

# 7. Create a Rectangle Class

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def display_rectangle(self):
        print("Length:", self.length)
        print("Width:", self.width)
r1 = Rectangle(10, 5)

r1.display_rectangle()

# 8. Create a Circle Class

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def display_circle(self):
        print("Radius:", self.radius)

c1 = Circle(7)

c1.display_circle()

# 9. Create an Employee Class

class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def display_employee(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)
e1 = Employee("Amit", 50000, "IT")

e1.display_employee()

# 10. Create a Movie Class

class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def display_movie(self):
        print("Title:", self.title)
        print("Director:", self.director)
        print("Year:", self.year)
m1 = Movie("3 Idiots", "Rajkumar Hirani", 2009)

m1.display_movie()

# 11. Create a Company Class

class Company:
    company_name = "Google"

    def __init__(self, employee_name):
        self.employee_name = employee_name

    def display_company(self):
        print("Company Name:", Company.company_name)
        print("Employee Name:", self.employee_name)
comp1 = Company("Rohit")

comp1.display_company()

# 12. Create a Bank Class

class Bank:
    bank_name = "State Bank of India"

    def __init__(self, customer_name, balance):
        self.customer_name = customer_name
        self.balance = balance

    def display_bank(self):
        print("Bank Name:", Bank.bank_name)
        print("Customer Name:", self.customer_name)
        print("Balance:", self.balance)
b1 = Bank("Ravi", 50000)

b1.display_bank()

# 13. Create a School Class

class School:
    school_name = "ABC Public School"

    def __init__(self, student_name, class_name):
        self.student_name = student_name
        self.class_name = class_name

    def display_school(self):
        print("School Name:", School.school_name)
        print("Student Name:", self.student_name)
        print("Class Name:", self.class_name)
s1 = School("Aman", "10th")

s1.display_school()

# 14. Create a College Class

class College:
    college_name = "IIT Delhi"

    def __init__(self, student_name, branch):
        self.student_name = student_name
        self.branch = branch

    def display_college(self):
        print("College Name:", College.college_name)
        print("Student Name:", self.student_name)
        print("Branch:", self.branch)
clg1 = College("Rohit", "Computer Science")

clg1.display_college()

# 15. Create a Hospital Class

class Hospital:
    hospital_name = "City Hospital"

    def __init__(self, patient_name, disease):
        self.patient_name = patient_name
        self.disease = disease

    def display_hospital(self):
        print("Hospital Name:", Hospital.hospital_name)
        print("Patient Name:", self.patient_name)
        print("Disease:", self.disease)
h1 = Hospital("Karan", "Fever")

h1.display_hospital()

# 16. Create a Person Class

class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def display_person(self):
        print("Name:", self.name)
        print("City:", self.city)
p1 = Person("Rohit", "Jodhpur")

p1.display_person()

# 17. Create a Fruit Class

class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def display_fruit(self):
        print("Fruit Name:", self.name)
        print("Color:", self.color)
f1 = Fruit("Apple", "Red")

f1.display_fruit()

# 18. Create a Pen Class

class Pen:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display_pen(self):
        print("Brand:", self.brand)
        print("Price:", self.price)
p1 = Pen("Cello", 20)

p1.display_pen()

# 19. Create a Fan Class

class Fan:
    def __init__(self, brand, speed, price):
        self.brand = brand
        self.speed = speed
        self.price = price

    def display_fan(self):
        print("Brand:", self.brand)
        print("Speed:", self.speed)
        print("Price:", self.price)
f1 = Fan("Usha", 5, 2500)

f1.display_fan()

# 20.Create a TV Class

class TV:
    category = "Electronics"

    def __init__(self, brand, size, price):
        self.brand = brand
        self.size = size
        self.price = price

    def display_tv(self):
        print("Category:", TV.category)
        print("Brand:", self.brand)
        print("Size:", self.size)
        print("Price:", self.price)

tv1 = TV("Sony", "43 Inch", 45000)
tv2 = TV("Samsung", "55 Inch", 65000)

tv1.display_tv()
print()

tv2.display_tv()

# 21.Create a BankAccount Class

class BankAccount:
    bank_name = "HDFC Bank"

    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def display_account(self):
        print("Bank Name:", BankAccount.bank_name)
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)
a1 = BankAccount("Rohit", 1001, 50000)
a2 = BankAccount("Amit", 1002, 70000)
a3 = BankAccount("Ravi", 1003, 90000)

a1.display_account()
print()

a2.display_account()
print()

a3.display_account()

# class creation with constructur and display all detail 
# 
# 
# 
# and from update and more tasks

#1. studnet management system
class Student:
  def __init__(self,id,name,age,marks):
    self.id=id
    self.name=name
    self.age=age
    self.marks=marks
  def display(self):
    print(f"Studnet_id {self.id}")
    print(f"Studnet_name {self.name}")
    print(f"Studnet_age {self.age}")
    print(f"Studnet_marks {self.marks}")

  def update_marks(self,new_marks):
    self.marks=new_marks

  def change_course(self,new_courese):
    self.course=new_course
  def is_pass(self):
    if self.marks>=40:
      print("pass")
    else:
      print("fail")

a=Student(1,"rohit",22,85,)
a.display()
a.update_marks(90)
a.display()
a.is_pass()
# a.display()
# a.update_marks(90)
# a.is_pass()

# 2. employee management syatem
class Employee:
  def __init__(self,Emp_id,emp_name,emp_age,emp_salary):
    self.id=Emp_id
    self.name=emp_name
    self.age=emp_age
    self.salary=emp_salary
  def display(self):
    print(f"Emp_id {self.id}")
    print(f"Emp_name {self.name}")
    print(f"Emp_age {self.age}")
    print(f"Emp_salary {self.salary}")
  def update_salary(self,new_salary):
    self.salary=new_salary
  def change_department(self,new_department):
    self.department=new_department
  def calculate_anualsalary(self):
    print("your salary anual_salary is :",self.salary*12)

rohit=Employee(1,"rohit",22,50000)
rohit.display()
rohit.update_salary(60000)
rohit.display()
rohit.calculate_anualsalary()

#3. Library Management System
class Library:
  def __init__(self,book_id,titel,author,availability_status):
    self.id=book_id
    self.titel=titel
    self.author=author
    self.availability=availability_status
  def display(self):
    print(f"book_id {self.id}")
    print(f"book_titel {self.titel}")
    print(f"book_author {self.author}")
    print(f"book_availability {self.availability}")
  def issue(self,issue_status):
    self.availability=issue_status
  def change_tital(self,new_tital):
    self.titel=new_tital

name=Library(1,"name","rohit","yes")
name.display()
name.issue("no")
name.display()

# Bank Account Management System
class Bank_account:
  def __init__(self,account_number,account_holder_name,balance):
    self.account_number=account_number
    self.account_holder_name=account_holder_name
    self.balance=balance
  def display(self):
    print(f"account_number {self.account_number}")
    print(f"account_holder_name {self.account_holder_name}")
    print(f"balance {self.balance}")
  def diposite_amount(self,amount):
    self.balance+=amount
  def withdraw_amount(self,amount):
    if self.balance>=amount:
      self.balance-=amount
    else:
      print("insufficient balance")

account_holder=Bank_account(123456789,"rohit",10000)
account_holder.display()
account_holder.diposite_amount(5000)
account_holder.display()
account_holder.withdraw_amount(2000)
account_holder.display()

# Hospital Management System
class Hospital:
  def __init__(self,patient_id,patient_name,patient_disease,doctor_assigen):
    self.id=patient_id
    self.name=patient_name
    self.patient_disease=patient_disease
    self.doctor_name=doctor_assigen
    self.dischare_patient=False
  def display_patient_detail(self):
    print(f"patient_id {self.id}")
    print(f"patient_name {self.name}")
    print(f"patient_disease {self.patient}")
  def new_disese(self,new_disese):
    self.patient_disease=new_disese
  def doctor_assigen(self,new_doctor):
    self.doctor_name=new_doctor
  def discharge_patients(self,discharge_patients):
    if discharge_patients=="yes":
      self.dischare_patient=True
    else:
      self.dischare_patient=False

patient=Hospital

# 6. Product Inventory Management System

class Product:
    def __init__(self, product_id, product_name, price, quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def display_product(self):
        print("Product ID:", self.product_id)
        print("Product Name:", self.product_name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

    def update_price(self, new_price):
        self.price = new_price
        print("Price updated successfully.")

    def add_stock(self, quantity):
        self.quantity += quantity
        print(quantity, "items added to stock.")

    def sell_product(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity
            print(quantity, "items sold.")
        else:
            print("Not enough stock available.")



p1 = Product(101, "Laptop", 50000, 10)

p1.display_product()
p1.add_stock(5)
p1.sell_product(3)
p1.update_price(48000)
p1.display_product()

# 7. Car Rental Management System

class Car:
    def __init__(self, car_number, model, rent_per_day, availability=True):
        self.car_number = car_number
        self.model = model
        self.rent_per_day = rent_per_day
        self.availability = availability

    def display_car(self):
        print("Car Number:", self.car_number)
        print("Model:", self.model)
        print("Rent Per Day:", self.rent_per_day)
        print("Availability:", self.availability)

    def rent_car(self):
        if self.availability:
            self.availability = False
            print("Car rented successfully.")
        else:
            print("Car is already rented.")

    def return_car(self):
        self.availability = True
        print("Car returned successfully.")

    def change_rent(self, new_rent):
        self.rent_per_day = new_rent
        print("Rent updated successfully.")



c1 = Car("RJ14AB1234", "Swift", 1500)

c1.display_car()
c1.rent_car()
c1.return_car()
c1.change_rent(1800)

# 8. Hotel Room Management System

class Room:
    def __init__(self, room_number, room_type, price_per_night, booking_status=False):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.booking_status = booking_status

    def display_room(self):
        print("Room Number:", self.room_number)
        print("Room Type:", self.room_type)
        print("Price Per Night:", self.price_per_night)
        print("Booking Status:", self.booking_status)

    def book_room(self):
        if not self.booking_status:
            self.booking_status = True
            print("Room booked successfully.")
        else:
            print("Room already booked.")

    def checkout_room(self):
        self.booking_status = False
        print("Checkout completed.")

    def update_price(self, new_price):
        self.price_per_night = new_price
        print("Room price updated.")


r1 = Room(201, "Deluxe", 3000)

r1.display_room()
r1.book_room()
r1.checkout_room()
r1.update_price(3500)

# 9. Online Course Management System

class Course:
    def __init__(self, course_id, course_name, instructor, fee):
        self.course_id = course_id
        self.course_name = course_name
        self.instructor = instructor
        self.fee = fee

    def display_course(self):
        print("Course ID:", self.course_id)
        print("Course Name:", self.course_name)
        print("Instructor:", self.instructor)
        print("Fee:", self.fee)

    def change_instructor(self, new_instructor):
        self.instructor = new_instructor
        print("Instructor changed successfully.")

    def update_fee(self, new_fee):
        self.fee = new_fee
        print("Fee updated successfully.")

    def apply_discount(self, percent):
        discount = self.fee * percent / 100
        self.fee -= discount
        print("Discount applied.")



course1 = Course(1, "Python", "Rohit Sir", 5000)

course1.display_course()
course1.apply_discount(10)
course1.change_instructor("Amit Sir")
course1.display_course()

# 10. Movie Ticket Booking System

class Movie:
    def __init__(self, movie_name, show_time, ticket_price, available_seats):
        self.movie_name = movie_name
        self.show_time = show_time
        self.ticket_price = ticket_price
        self.available_seats = available_seats

    def display_movie(self):
        print("Movie Name:", self.movie_name)
        print("Show Time:", self.show_time)
        print("Ticket Price:", self.ticket_price)
        print("Available Seats:", self.available_seats)

    def book_ticket(self, number_of_seats):
        if number_of_seats <= self.available_seats:
            self.available_seats -= number_of_seats
            print(number_of_seats, "tickets booked.")
        else:
            print("Not enough seats available.")

    def cancel_ticket(self, number_of_seats):
        self.available_seats += number_of_seats
        print(number_of_seats, "tickets cancelled.")

    def change_show_time(self, new_time):
        self.show_time = new_time
        print("Show time updated.")



m1 = Movie("Avengers", "7 PM", 250, 100)

m1.display_movie()
m1.book_ticket(5)
m1.cancel_ticket(2)
m1.change_show_time("9 PM")

# 11. Restaurant Order Management System

class MenuItem:
    def __init__(self, item_id, item_name, price, quantity_available):
        self.item_id = item_id
        self.item_name = item_name
        self.price = price
        self.quantity_available = quantity_available

    def display_item(self):
        print("Item ID:", self.item_id)
        print("Item Name:", self.item_name)
        print("Price:", self.price)
        print("Quantity Available:", self.quantity_available)

    def update_price(self, new_price):
        self.price = new_price
        print("Price updated.")

    def place_order(self, quantity):
        if quantity <= self.quantity_available:
            self.quantity_available -= quantity
            print("Order placed successfully.")
        else:
            print("Insufficient quantity.")

    def restock(self, quantity):
        self.quantity_available += quantity
        print("Stock updated.")



item1 = MenuItem(1, "Burger", 120, 50)

item1.display_item()
item1.place_order(5)
item1.restock(10)

# 12. Gym Membership Management System

class Member:
    def __init__(self, member_id, name, membership_type, fee):
        self.member_id = member_id
        self.name = name
        self.membership_type = membership_type
        self.fee = fee

    def display_member(self):
        print("Member ID:", self.member_id)
        print("Name:", self.name)
        print("Membership Type:", self.membership_type)
        print("Fee:", self.fee)

    def upgrade_membership(self, new_type, new_fee):
        self.membership_type = new_type
        self.fee = new_fee
        print("Membership upgraded.")

    def renew_membership(self):
        print("Membership renewed successfully.")

    def change_name(self, new_name):
        self.name = new_name
        print("Name updated.")



mem1 = Member(101, "Rohit", "Basic", 2000)

mem1.display_member()
mem1.upgrade_membership("Premium", 5000)
mem1.change_name("Rohit Sharma")

# 13. Mobile Phone Management System

class MobilePhone:
    def __init__(self, brand, model, price, storage):
        self.brand = brand
        self.model = model
        self.price = price
        self.storage = storage

    def display_phone(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)
        print("Storage:", self.storage)

    def update_price(self, new_price):
        self.price = new_price
        print("Price updated.")

    def upgrade_storage(self, new_storage):
        self.storage = new_storage
        print("Storage upgraded.")

    def apply_discount(self, percent):
        discount = self.price * percent / 100
        self.price -= discount
        print("Discount applied.")



phone1 = MobilePhone("Samsung", "S24", 80000, "128GB")

phone1.display_phone()
phone1.apply_discount(5)
phone1.upgrade_storage("256GB")

# 14. School Bus Management System

class Bus:
    def __init__(self, bus_number, driver_name, route, total_seats):
        self.bus_number = bus_number
        self.driver_name = driver_name
        self.route = route
        self.total_seats = total_seats

    def display_bus(self):
        print("Bus Number:", self.bus_number)
        print("Driver Name:", self.driver_name)
        print("Route:", self.route)
        print("Total Seats:", self.total_seats)

    def change_driver(self, new_driver):
        self.driver_name = new_driver
        print("Driver changed.")

    def update_route(self, new_route):
        self.route = new_route
        print("Route updated.")

    def check_seat_availability(self, booked_seats):
        available = self.total_seats - booked_seats
        print("Available Seats:", available)



b1 = Bus("RJ19PA1234", "Mahesh", "School to City", 40)

b1.display_bus()
b1.change_driver("Suresh")
b1.update_route("New Route")
b1.check_seat_availability(15)

# 15. E-Commerce Order Management System

class Order:
    def __init__(self, order_id, customer_name, product_name, order_status):
        self.order_id = order_id
        self.customer_name = customer_name
        self.product_name = product_name
        self.order_status = order_status

    def display_order(self):
        print("Order ID:", self.order_id)
        print("Customer Name:", self.customer_name)
        print("Product Name:", self.product_name)
        print("Order Status:", self.order_status)

    def update_status(self, new_status):
        self.order_status = new_status
        print("Order status updated.")

    def change_product(self, new_product):
        self.product_name = new_product
        print("Product changed successfully.")

    def cancel_order(self):
        self.order_status = "Cancelled"
        print("Order cancelled.")



o1 = Order(1001, "Rohit", "Laptop", "Pending")

o1.display_order()
o1.update_status("Shipped")
o1.change_product("Gaming Laptop")
o1.cancel_order()
o1.display_order()

