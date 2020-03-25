### F string

name = "Bob"
greeting = f"Hello, {name}"

print(greeting)

#### format template

greeting = "Hello, {}. Today is {}"
with_name = greeting.format("Bob", "Monday")

print(with_name)

square_feet = 500
square_metres = square_feet / 10.8
print(f"{square_feet} square feet is {square_metres:.2f} sqaure metres.") ## .2f to round the number 

### tuple

single_value_tuple = 15, # or (15, )

### advanced set operations

friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad) ## it removes the items in abroad from friends
print(f"local: {local_friends}")
print(f"Common: {friends.intersection(abroad)}") ## it gets the elements in commmon

local = {"Rolf"}
abroad = {"Bob", "Anne"}

friends = local.union(abroad)
print(f"friends: {friends}")

### comparation

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

print(friends == abroad) ## compares values
print(friends is abroad) ## compare memory address

### String
print("LOWER-CASE".lower())

### Dictionaries

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
for student, attendance in student_attendance.items():
    print(f"Student {student} attendance is {attendance}%")

### Destructuring values

head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)

def add(x, y):
    return x + y

nums = [3, 5]
print(add(*nums))

nums = {"x": 15, "y":25}
print(add(**nums))

def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
    return total

def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()"

print(apply(1, 2, 3, 4 , 5, operator="+"))

def named(**kwargs):
    print(kwargs)

named(name="Bob", age=24)

### OO

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Student: {self.name}, average grade: {self.average()}"

    def __repr__(self):
        return f"<Person({self.name}, {self.grades})>"

student = Student("Rolf", (90, 90, 93,78, 90))
print(Student.average(student))
print(student.average())
print(student)

class ClassTest:
    TYPES = ("hardcover", "paperback")

    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_methdo of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method")        

class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, {self.weight} >"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)    


book = Book("Harry Potter", "hardcover", 1500)
book2 = Book.hardcover("Harry Potter", 1500)
book3 = Book.paperback("Harry Potter", 1500)
print(book)
print(book2)
print(book3)

## Inheritance

class Device:
    def __init__(self, naem, connecteced_by):
        self.name = name
        self.connecteced_by = connecteced_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connecteced_by})"

    def disconnect(self):
        self.connecteced =False

class Printer(Device):
    def __init__(self, name, connecteced_by, capacity):
        super().__init__(name, connecteced_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages

printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)

printer.disconnect()
printer.print(30)
