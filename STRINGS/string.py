# Task 1 — Create Strings

name = "Naman"
city = 'Kalol'
favorite_language = "Python"
message = 'Python is easy to learn.'

print(name)
print(city)
print(favorite_language)
print(message)


# Task 2 — Empty String

text = ""

print(text)
print(len(text))
print(type(text))


# Task 3 — String Information

text = "Python Programming"

print(text)
print(len(text))
print(text[0])
print(text[-1])
print(text[2])
print(text[-2])


# Task 4 — Positive Indexing

text = "Programming"

print(text[0])
print(text[1])
print(text[4])
print(text[10])


# Task 5 — Negative Indexing

text = "Programming"

print(text[-1])
print(text[-2])
print(text[-3])
print(text[-11])


# Task 6 — Indexing Challenge

full_name = "Naman Soni"

print(full_name[0])
print(full_name[-1])
print(full_name[6])


# Task 7 — Basic Slicing

text = "Python Programming"

print(text[0:6])
print(text[7:18])
print(text[:])
print(text[0:5])
print(text[-5:])


# Task 8 — Slicing with Step

text = "ABCDEFGHIJKL"

print(text[::2])
print(text[::3])
print(text[1:9:2])
print(text[::-1])


# Task 9 — Slicing with Negative Indexes

text = "Python Programming"

print(text[-5:])
print(text[-10:])
print(text[::-2])


# Task 10 — Slicing Challenge

text = "Programming"

print(text[:3])
print(text[-3:])
print(text[::2])
print(text[::-1])
print(text[1:-1])


# Task 11 — Length

word = "Python"
sentence = "Python is easy."
sentence_with_spaces = "Python is very easy to learn."

print(len(word))
print(len(sentence))
print(len(sentence_with_spaces))


# Task 12 — Last Valid Positive Index

text = "Python Programming"

last_index = len(text) - 1

print(last_index)
print(text[last_index])


# Task 13 — Full Name

first_name = "Naman"
last_name = "Soni"

full_name = first_name + " " + last_name

print(full_name)


# Task 14 — Sentence Creation

name = "Naman"
age = 18
city = "Kalol"
programming_language = "Python"

sentence = (
    name + " is " + str(age) + " years old and lives in "
    + city + ". He is learning " + programming_language + "."
)

print(sentence)


# Task 15 — String and Integer

name = "Naman"
age = 18

# print(name + age)  # TypeError

print(name + str(age))


# Task 16 — String Repetition

symbol = "*"

print(symbol * 3)
print(symbol * 5)
print(symbol * 10)


# Task 17 — Pattern

symbol = "*"

print(symbol * 10)


# Task 18 — Case Conversion

text = "python programming language"

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.swapcase())


# Task 19 — Case-Insensitive Comparison

text1 = "Python"
text2 = "python"

print(text1 == text2)
print(text1.lower() == text2.lower())


# Task 20 — Membership

text = "Python is a programming language"

print("Python" in text)
print("programming" in text)
print("Java" in text)
print("language" in text)


# Task 21 — find()

text = "Python is a programming language"

print(text.find("Python"))
print(text.find("programming"))
print(text.find("language"))
print(text.find("Java"))


# Task 22 — index()

text = "Python is a programming language"

print(text.index("Python"))
print(text.index("programming"))
print(text.index("language"))

# Java is not present, so index() produces ValueError.
# print(text.index("Java"))


# Task 23 — Count Characters

text = "banana"

print(text.count("a"))
print(text.count("n"))
print(text.count("b"))


# Task 24 — Starts and Ends

filename = "student_notes.pdf"

print(filename.startswith("student"))
print(filename.endswith(".pdf"))
print(filename.endswith(".txt"))


# Task 25 — Replace a Word

text = "I am learning Java"

new_text = text.replace("Java", "Python")

print(new_text)


# Task 26 — Multiple Replacements

text = "apple apple apple"

new_text = text.replace("apple", "mango")

print(new_text)


# Task 27 — Limited Replacement

text = "apple apple apple"

new_text = text.replace("apple", "mango", 1)

print(new_text)


# Task 28 — Check Immutability

text = "Python"

text.upper()

print(text)

text = text.upper()

print(text)


# Task 29 — Whitespace

text = "   Python Programming   "

print(text.strip())
print(text.lstrip())
print(text.rstrip())


# Task 30 — User Input

name = input("Enter your name: ")

cleaned_name = name.strip()

print(cleaned_name)


# Task 31 — Split

text = "Python is easy to learn"

words = text.split()

print(words)


# Task 32 — Split with Separator

text = "apple,banana,mango,orange"

fruits = text.split(",")

print(fruits)


# Task 33 — Join

words = ["Python", "is", "easy"]

sentence = " ".join(words)

print(sentence)


# Task 34 — Join with Different Separators

words = ["Python", "is", "easy"]

print("-".join(words))
print("/".join(words))


# Task 35 — F-String

name = "Naman"
age = 18
city = "Kalol"

sentence = f"My name is {name}, I am {age} years old, and I live in {city}."

print(sentence)


# Task 36 — Arithmetic Inside F-String

a = 10
b = 20

print(f"The sum is {a + b}")


# Task 37 — Error Identification

# A — IndexError
text = "Python"

try:
    print(text[20])
except IndexError:
    print("IndexError: String index is out of range.")


# B — TypeError
text = "Python"

try:
    text[0] = "J"
except TypeError:
    print("TypeError: Strings cannot be changed directly.")


# C — TypeError
age = 20

try:
    print("Age: " + age)
except TypeError:
    print("TypeError: Cannot concatenate string and integer.")


# D — ValueError
text = "Python"

try:
    print(text.index("Java"))
except ValueError:
    print("ValueError: Substring not found.")


# Task 38 — Name Processor

full_name = input("Enter your full name: ")

cleaned_name = full_name.strip()

print("Original input:", full_name)
print("Cleaned name:", cleaned_name)
print("Uppercase:", cleaned_name.upper())
print("Lowercase:", cleaned_name.lower())
print("Title case:", cleaned_name.title())
print("Length:", len(cleaned_name))
print("First character:", cleaned_name[0])
print("Last character:", cleaned_name[-1])
print("Contains 'a':", "a" in cleaned_name.lower())


# Task 39 — Sentence Analyzer

sentence = input("Enter a sentence: ")
chosen_character = input("Enter a character to count: ")

print("Original sentence:", sentence)
print("Number of characters:", len(sentence))
print("Number of words:", len(sentence.split()))
print("First character:", sentence[0])
print("Last character:", sentence[-1])
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Title case:", sentence.title())
print("Contains 'Python':", "Python" in sentence)
print("Character count:", sentence.count(chosen_character))


# Task 40 — Student Information

first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
city = input("Enter city: ").strip()
course = input("Enter course: ").strip()
age = input("Enter age: ").strip()

full_name = first_name + " " + last_name

print("Full name:", full_name.title())
print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())
print("Length:", len(full_name))
print("First character:", full_name[0])
print("Last character:", full_name[-1])
print("City:", city)
print("Course:", course)
print(f"Age: {age}")
print("Course contains Python:", "Python" in course)

updated_course = course.replace("Java", "Python", 1)
print("Updated course:", updated_course)

print("Number of words in course:", len(course.split()))
