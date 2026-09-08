# ==========================================
# Python Conditional Statements
# Questions 16 to 30
# ==========================================

# 16. Age between 18 and 60
print("\n--- Question 16 ---")
age = int(input("Enter age: "))

if age >= 18:
    if age <= 60:
        print("Between 18 and 60")


# 17. Marks Check
print("\n--- Question 17 ---")
marks = int(input("Enter marks: "))

if marks >= 40:
    if marks >= 75:
        print("Good")
    else:
        print("Passed")
else:
    print("Failed")


# 18. Positive and Greater Than 100
print("\n--- Question 18 ---")
number = int(input("Enter a number: "))

if number > 0:
    if number > 100:
        print("Greater than 100")
    else:
        print("Positive but not greater than 100")
else:
    print("Not positive")


# 19. Age Check
print("\n--- Question 19 ---")
age = int(input("Enter age: "))

if age >= 18:
    if age >= 60:
        print("Senior citizen")
    else:
        print("Adult")
else:
    print("Minor")


# 20. Non-zero, Positive or Negative
print("\n--- Question 20 ---")
number = int(input("Enter a number: "))

if number != 0:
    if number > 0:
        print("Positive")
    else:
        print("Negative")
else:
    print("Zero")


# 21. Age and Marks
print("\n--- Question 21 ---")
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))

if age >= 18 and marks >= 40:
    print("Eligible")


# 22. Special Number
print("\n--- Question 22 ---")
number = int(input("Enter a number: "))

if number < 10 or number > 100:
    print("Special")


# 23. Age and ID
print("\n--- Question 23 ---")
age = int(input("Enter age: "))
has_id = input("Do you have ID? (True/False): ")

has_id = has_id == "True"

if age >= 18 and has_id is True:
    print("Allowed")


# 24. Both Numbers Greater Than 10
print("\n--- Question 24 ---")
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

if first > 10 and second > 10:
    print("Both are greater than 10")


# 25. Less Than 0 or Greater Than 100
print("\n--- Question 25 ---")
number = int(input("Enter a number: "))

if number < 0 or number > 100:
    print("Number is outside the range")


# 26. Using NOT
print("\n--- Question 26 ---")
is_closed = False

if not is_closed:
    print("Open")


# 27. Between 10 and 50
print("\n--- Question 27 ---")
number = int(input("Enter a number: "))

if number >= 10 and number <= 50:
    print("Number is between 10 and 50")


# 28. Outside 10 to 50
print("\n--- Question 28 ---")
number = int(input("Enter a number: "))

if number < 10 or number > 50:
    print("Number is outside 10 to 50")


# 29. Student, ID and Ticket
print("\n--- Question 29 ---")
is_student = True
has_id = True
has_ticket = True

if is_student and has_id and has_ticket:
    print("Allowed")


# 30. Eligibility Checker
print("\n--- Question 30 ---")
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))
has_id = input("Do you have ID? (True/False): ")

has_id = has_id == "True"

if age >= 18 and marks >= 40 and has_id is True:
    print("Eligible")
else:
    print("Not eligible")