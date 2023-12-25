'''
Python - Selenium | Functions and Classes


A function is a named block of code that performs a 
specific task or a set of instructions. Functions provide a way 
to modularize and organize code, making it easier to reuse, test, and maintain.
Indentation is highly required in functions.

A class is a blueprint or a template for creating objects. It defines a set of 
attributes (variables) and methods (functions) that the objects of the class will have. 
Classes provide a way to define and create objects with specific properties and behaviors.
Class names must start with upper case.

"self" is a conventionally used parameter name that refers to the instance of a 
class. It represents the object itself and is used within class methods to access and 
manipulate the attributes and methods of that object.

'''

class Bank:
	def creditApplication(self):
		# self = this
		print("Credit applicaiton is on process")

	def calculateCredits(self):
		print("Calculation is on process")

if __name__ == "__main__":
	bank = Bank()
	bank.creditApplication()
	bank.calculateCredits()


'''
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        #print("People are here")


if __name__ == "__main__":
      client1 = Person("Charles", "Leclerc")
      client2 = Person("Max", "Verstappen")
      client3 = Person("Lewis", "Hamilton")
      print(client1.name)
      print(client2.name)
      print(client3.name)
      
'''

