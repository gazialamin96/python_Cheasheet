print("Hello There! I Al- Amin and i am here to introduce you python basis with advance")
print("Now starting with what is python?")
print("Python is an object-oriented high-level programming language. It was first published by Guido van Rossum in 1991")
print("When creating Python, program readability was given a lot of importance.")
print("Here the work of the programmer is given more importance than the computer")

print("Now introducing python variable's: ")
print("Variables are containers for holding data values.")

""" 
Variables 
"""
cost = 10  # integer variable
tax_percent = .20  # float variable
tax = cost * tax_percent
price = cost + tax

print(price)

"""
String variables
"""
username = "codingwithgazi"
print(username)  # print the string variable

first_name = "Gazi"
last_name = "Al- Amin"
"""
Print and concatenate the string values (String Formatting)
"""
print("Hi! Your username: " + username + " your First Name is: " + first_name + ", & your Last Name is: " + last_name)

# Another way we can print using f string before double quotation
print(f"Hi! Your username: {username} your First Name is: {first_name}, & your Last Name is: {last_name}")

# also other way we can use this
sentence = "Hi! Your username: {} your First Name is: {}, & your Last Name is: {}"
print(sentence.format(username, first_name, last_name))
# all strings formatting have same outputs


"""
Comment's
"""

# This is Single Line Comments

"""
This is Multi-Line
Comment's with 
three double quotation marks
"""

'''
This is another way
 we can create multi-line comments 
 with three Single quotation marks
'''

"""
Assignment Operator's : Assignment operators are used to assign values to variables
"""

'''
--- Let's Think---
- you have $200
- you buy an item that is $100
- with a tax of 5%
- print how much money you have left
'''
youHave = 200  # Operator Assignment (=)
buyItem = 100  # Operator Assignment (=)
taxOfBoughtItem = .05  # float value of the variable bought item

boughtItemTotalCost = buyItem + (buyItem * taxOfBoughtItem)

leftMoney = youHave - boughtItemTotalCost

print(leftMoney)

# Operator Addition (+=)
x = 5
x += 1  # it will be written another way like (x= x+1)
print(x)

# operator subtractions
y = 10
y -= 2  # y= y-2
print(y)  # result: 8

# Operator Multiplication (*=)
z = 5
z *= 2
print(z)  # Result: 10

# Operator Division (/=)
p = 200
p /= 2
print(p)  # Result: 100

# Operator Modulus (%=)
q = 4
q %= 3
print(q)  # result: 1

# Operator Exponentiation (**=)
r = 2
r **= 4  # r= r**4 (** also called r to the power 4)
print(r)  # result: 16

# Operator Floor Division (//=)
s = 20
s //= 3  # s = s//3 (// quotient)
print(s)  # result: 6

"""
Boolean and Operator
"""
# Comparison Operator
print(1 == 2)
print(1 != 2)
print(1 > 2)
print(1 < 2)
print(1 >= 1)
print(1 >= 2)
# all have output either true or false

# Logical operator
print(1 > 3 and 5 < 7)
print(1 > 3 or 5 < 7)
print(not (1 == 1))

"""
User Input
"""
employee_Name = input("Enter Employee Name: ")  # this will be string type input
employee_Date_of_Birth = input("Enter Employee Date of Birth: ")  # this will be string type input
employee_Joining_Date = input("Enter joining date of Employee: ")  # this will be string type input
# integer input with an integer wrapper
# int will convert from string to int we also called it type casting
employee_Age = int(input("Enter Employee Age: "))

# now print all the employee information to the console
# using f string what we already learn
print(f"Employee name is: {employee_Name}\n {employee_Name}'s Date Of Birth is: {employee_Date_of_Birth}\n"
      f"{employee_Name}'s Age is: {employee_Age}\n {employee_Name}'s Joining Date is: {employee_Joining_Date}\n")

'''
Lists: Lists are collection of data
'''
my_List = [10, 20, 30, 40, 50]
print(my_List)  # print that lists
print(len(my_List))  # print length of the Lists
my_List.append(1000)  # added value to lists
print(my_List)  # print with Added value
my_List.insert(3, 80)  # 3 is the index number and 80 is the object/ value
print(my_List)


# Slicing: slicing means you're only going to present specific data if the list that you want to show
print(my_List[2:4])  # it will show until index number 4 result: [30, 80]
print(my_List[0:-0])  # it will show null value like this []
print(my_List[0:0])  # also it will show null value like this []
print(my_List[0:-3])  # last three will be deducted result should be [10, 20, 30, 80]

my_List.remove(1000)  # it will remove 1000 value from the list, and it will check from index number 0
print(my_List)
my_List.pop(0)  # it will remove using index number
print(my_List)
my_List.sort()  # it will sort my_List values to ascending order
print(my_List)

"""
Sets are similar to Lists but sets are unordered and 
cannot contains duplicates 
it also using curly brackets
it will contains only unique values
"""
my_Set = {1, 2, 3, 4, 5, 1, 3}
print(my_Set)  # result will be {1, 2, 3, 4, 5} because it will contains only unique values
print(len(my_Set))  # it also contains only unique values length

my_Set.discard(2)  # it will be remove 2
print(my_Set)
my_Set.add(6)  # it will add 6 to the set
print(my_Set)
my_Set.update([7, 8])  # to update set 7, 8
print(my_Set)


"""
Tuple 
Tuple are ordered just like lists, but they're unchangeable
it using parenthesis
"""
my_Tuple = (11, 12, 13, 14, 15)  # tuples are not allowed to add, delete or remove anything the tuples
print(my_Tuple)


"""
Flow control: IF ELSE ELIF statement 
"""

hours = 13
if hours < 15:
      print(" Good Morning")
elif hours < 20:
      print("Good Afternoon")
else:
      print("Good Night!")


"""
Solve this problem with if else elif statement

Grades:
A = 90 - 100
B = 80 - 89
C = 70 - 79
D = 60 - 69
F = 0  - 59
"""
grade = 69
if (grade >= 90) and (grade <= 100):
      print("A")
elif (grade >= 80) and (grade <= 89):  # also we can write it 80 <= grade <90
      print("B")
elif (grade >= 70) and (grade <= 79):
      print("C")
elif (grade >= 60) and (grade <= 69):
      print("D")
elif (grade >= 0) and (grade <= 59):
      print("F")
else:
      print("Please, type the valid number!")

