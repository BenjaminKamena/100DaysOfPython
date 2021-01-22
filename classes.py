class Students():
     district = 'mufumbwe'
   def __init__(self, name, grade, school):
       self.name = name
       self.grade = grade
        self.school = school
    def best(self, grade):
        print('AAA The best student is {} and the grade is {}'.format(self.name, grade))
my_student = Students('Benjamin','g12','kashima high school')
my_student.name
my_student.grade
my_student.school
my_student.district
my_student.best('g13')


class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
    def circumference(self):
        return self.radius * self.pi * 2
my_circle = Circle(30)
my_circle.pi
my_circle.radius
my_circle.circumference()

class Animal():
    def __init__(self):
        print("ANIMAL CREATED")
    def who_am_i(self):
        print("I am an animal")
    def eat(self):
        print('i am eating')
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('DOG CREATED')
my_dog = Dog()
my_dog.eat()

class Dog():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name +" says woof!"

class Cat():
    def __init__(self, name):
       self.name = name
    def speak(self):
        return self.name +" says moew!"

benjamin = Dog("benjamin")
kumbuso = Cat("kumbuso")

print(benjamin.speak())
print(kumbuso.speak())

mylist = [1, 2, 3]
 len(mylist)

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.title} by {self.author}"
    def __len__(self):
        return self.pages

b = Book("python tricks", "benjamin", 200)
print(b)
print(len(b))


 class Account():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, dep_amt):
        self.balance = self.balance + dep_amt
        print(f"Added {dep_amt} to the balance")

    def withdrawal(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance = self.balance - wd_amt
            print("Withdrawal accepted")
        else:
            print("Sorry no enough funds!")
    def __str__(self):
        return f"Owner: {self.owner} \n Balance: {self.balance}"


bank = Account("Benjamin", 457)
print(bank.owner)
print(bank.balance)
bank.deposit(100)
print(bank.withdrawal(700))

# day16
from turtle import *

timmy = Turtle()
my_screen = Screen()
timmy.shape('turtle')
timmy.color('green', 'yellow')
timmy.begin_fill()
while True:
    timmy.forward(200)
    timmy.left(170)
    if abs(timmy.pos()) < 1:
        break;
timmy.end_fill()
timmy.done()

print(my_screen.canvheight)
my_screen.exitonclick()

from prettytable import  PrettyTable

table = PrettyTable()
table.add_column("Pokeman Name", ["Benjamin", "Kamena", "Chulu"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "c"

print(table)

