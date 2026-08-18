# ===== Basic Python Concepts =====

# 1. Variables and Data Types
name = "Alice"
age = 25
height = 5.6
is_student = True

print("=== Variables ===")
print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")

# 2. Basic Arithmetic
a = 10
b = 3
print("\n=== Arithmetic ===")
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Floor Division: {a // b}")
print(f"Modulus: {a % b}")

# 3. Conditional Statements
num = int(input("\nEnter a number: "))
print("=== Conditionals ===")
if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is zero")

# 4. Lists
fruits = ["apple", "banana", "orange", "mango"]
print("\n=== Lists ===")
print(f"Fruits: {fruits}")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
fruits.append("grape")
print(f"After adding grape: {fruits}")

# 5. Loops - For Loop
print("\n=== For Loop ===")
for fruit in fruits:
    print(f"  - {fruit}")

# 6. Loops - While Loop
print("\n=== While Loop ===")
count = 1
while count <= 3:
    print(f"Count: {count}")
    count += 1

# 7. Dictionary
person = {"name": "Bob", "age": 30, "city": "New York"}
print("\n=== Dictionary ===")
print(f"Person: {person}")
print(f"Name: {person['name']}, Age: {person['age']}")

# 8. Function Definition
def greet(name):
    """This function greets someone"""
    return f"Hello, {name}!"

print("\n=== Functions ===")
print(greet("Charlie"))

# 9. String Methods
text = "Python Programming"
print("\n=== String Methods ===")
print(f"Lowercase: {text.lower()}")
print(f"Uppercase: {text.upper()}")
print(f"Length: {len(text)}")

# 10. List Comprehension
squares = [x**2 for x in range(1, 6)]
print("\n=== List Comprehension ===")
print(f"Squares of 1-5: {squares}")
    
    
    