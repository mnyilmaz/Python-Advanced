'''
Let's say we are writing a student registration system. Let's keep the students in our system in a list with only name and surname.

This student registration system;
  - Adding a student to the list with the given name and surname
  - Removes the value matching the given name and surname from the list.
  - Making it possible to add multiple students to the list
  - Prints all students in the list one by one
  - Considering that the index number of the student in the list is accepted as the student number, it makes it possible to learn the student's number.
  - Make it possible to delete multiple students from the list (use a loop)

develop the functions and test each function in the console by calling it at least once. It is requested that one of the loops you will use in the homework is a for loop and one is a while loop.

'''

def add(name, surname):
    studentList.append(name + ' ' + surname)

def remove(name, surname, studentList):
    remove_name = name + ' ' + surname
    studentList[:] = list(filter(lambda item: item != remove_name, studentList)) # [:] modifies the local variable instead of forming a new one
    
def add_multiple():
    while True:
        answer = input("Do you want to add more students? (Y/N) ")
        if answer == 'Y':
               n = input("Please enter the name: ")
               s = input("Please enter the surname: ")
               add(n, s)
        elif answer == 'N':
              break
        
def get_ID(studenList):
     length = len(studenList)
     for i in range (length):
          print(f"ID of {studenList[i]} is {i + 1}")

def purge(studentList):
     print("Purification is on process...")
     while studentList:
          studentList.pop() # removes last element of the list
          
     
if __name__ == "__main__":
    studentList = ['Charles Leclerc', 'Max Verstappen', 'Toto Wolff', 'Christian Horner']
    name = input("Please enter the name: ")
    surname = input("Please enter the surname: ")
    add(name,surname)
    #remove(name,surname,studentList)
    add_multiple()
    get_ID(studentList)
    purge(studentList)
    for i in range (len(studentList)):
        print(studentList[i])
