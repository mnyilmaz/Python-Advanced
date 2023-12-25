'''
Python - Selenium | Functions and Classes - Math Class and Inheritance

Understanding the self parameter.

In Python, __init__ is a special method, also known as a constructor. 
It is automatically called when an object is created from a class. 
The __init__ method allows you to initialize the attributes of an 
object and perform any necessary setup or configuration. (Initialize)

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = 3.14 * radius ** 2

small_circle = Circle(5)
large_circle = Circle(10)


In object-oriented programming, a constructor is a special method within 
a class that is automatically called when an object is created from that 
class. It is used to initialize the object's attributes, perform any necessary 
setup, and ensure that the object is in a valid state upon creation.

'''

class Math:
    def __init__(self): # constructor
         # self.num1 = num1 -> if you desire to run all these function upon 2 numbers use this method
         # self.num2 = num2
         print("Math class has started (reference occurred)")

    def add(self, num1, num2):
        # return self.num1 + self.num2
        return num1 + num2

    def subtract(self, num1, num2):
        # return self.num1 - self.num2
        return num1 - num2

    def multiply(self, num1, num2):
        # return self.num1 * self.num2
        return num1 * num2

    def divide(self, num1, num2):
        # return self.num1 / self.num2
        return num1 / num2

if __name__ == "__main__":
    math = Math() # this parantheses process the __init__ process automatically
    # math = Math(6,7)

    print(f"Result of addition is: {math.add(3,4)}") # math.add()
    print(f"Result of subtraction is: {math.subtract(56,34)}") # math.subtract()
    print(f"Result of multiplication is: {math.multiply(234,7867)}") # math.multiply()
    print(f"Result of division is: {math.divide(390,32)}") # math.divide()

'''
Inheritance

Inheritance is a fundamental concept in object-oriented programming 
(OOP) that allows a class to inherit attributes and methods from 
another class. In Python, you can create a new class based on an 
existing class, called the superclass or parent class, and inherit 
its properties. The new class is called the subclass or child class.

class Superclass:
    def method(self):
        print("This is a method from the superclass.")

class Subclass(Superclass):
    def method(self):
        print("This is a method from the subclass.")
  
if __name__ == "__main__":
	obj = Subclass()
    obj.method()  # Output: This is a method from the subclass.

'''