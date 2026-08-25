#BASIC ARITHMETIC
#perform
a=10
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)


#INTEGER AND FLOAT
a=8
b=2.9
print(a+b, type(a+b))
print(a-b, type(a-b))
print(a*b, type(a*b))
print(a/b, type(a/b))
print(a/b, type(a//b))
print(a%b, type(a%b))
print(a**b, type(a**b))

#STUDENT MARKS
a_mark=20
b_mark=30
c_mark=40
#total marks
print(a_mark+b_mark+c_mark)
#average marks
print((a_mark+b_mark+c_mark)/3)

#Product Calculation
price = 250
quantity = 4
total_price=price*quantity
print(total_price)

#Even or Odd
number = 17
print(number%2)

#Division and Floor Division
a = 10
b = 3
print(a / b)
print(a // b)

a = -10
b = 3
print(a / b)
print(a // b)

#Negative Number Operations
a = -10
b = -3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

# Subtraction Edge Cases
print("Positive - Positive:", 10 - 5)
print("Positive - Negative:", 10 - (-5))
print("Negative - Positive:", -10 - 5)
print("Negative - Negative:", -10 - (-5))

#Floor Division Edge Cases
print("Positive // Positive:", 10 // 3)
print("Negative // Positive:", -10 // 3)
print("Positive // Negative:", 10 // -3)
print("Negative // Negative:", -10 // -3)

#Modulus Edge Cases
print("Positive % Positive:", 10 % 3)
print("Negative % Positive:", -10 % 3)
print("Positive % Negative:", 10 % -3)
print("Negative % Negative:", -10 % -3)

#PART4
#Operator Precedence
print(10 + 5 * 2)
print(20 - 4 / 2)
print(10 + 20 / 5 * 2)
print(2 + 3 * 4 ** 2)
print(100 - 20 // 5)

#Parentheses
print(10 + 5 * 2)
print((10 + 5) * 2)

print(20 - 10 / 2)
print((20 - 10) / 2)

print(2 + 3 * 4)
print((2 + 3) * 4)

#Boolean Arithmetic
a = True
b = False
print(a + b, type(a + b))
print(a - b, type(a - b))
print(a * b, type(a * b))
#print(a / b, type(a / b))
#print(a // b, type(a // b))
#print(a % b, type(a % b))
print(a ** b, type(a ** b))

#Task 14
print(True + 5)
print(False + 5)
print(True * 10)
print(False * 10)
print(True - 5)
print(False - 5)

#Part 6 — String Operations
#Task 15
first_name = "Naman"
last_name = "Soni"
print(first_name+last_name)

#Task 16
word = "Python"
print(word * 3)

#Task 17 — String Operations
string1 = "Hello"
string2 = "World"
number = 3

# String + String
print(string1 + string2)

# String - String
#print(string1 - string2)

# String * Integer
print(string1 * number)

# String / String
#print(string1 / string2)

#Task 18 — None Type
value = None
number = 10
#print(value + number)
#print(value - number)
#print(value * number)
#print(value / number)
#print(value // number)
#print(value % number)
#print(value ** number)

#Task 19 — Error Handling Practice
#1. Division by Zero
a = 10
b = 0
#print(a / b)
#2. Invalid String Arithmetic
string1 = "Hello"
string2 = "World"
#print(string1 - string2)
#3. Arithmetic with None
value = None
number = 10
#print(value + number)

#Task 20 — Mini Calculator
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

#Part 10 — Final Challenge
#Task 21 — Arithmetic Expression Analyzer
a = 10
b = -3
c = 2.5

print("1.", a + b)
print("2.", a - b)
print("3.", a * c)
print("4.", a / c)
print("5.", a // c)
print("6.", a % 3)
print("7.", a ** 2)
print("8.", (a + b) * c)
print("9.", a + b * c)
print("10.", (a - b) / c)
print("11.", a + c * b)
print("12.", (a + c) ** 2)



