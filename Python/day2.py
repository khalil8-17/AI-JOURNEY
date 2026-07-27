# ============================================
# DAY 2 PYTHON PRACTICE - CONDITIONALS & LOOPS
# ============================================

# SECTION 1: CONDITIONAL STATEMENTS (if, elif, else)
# ===================================================

# Practice 1: Simple if-else
age = 15
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Practice 2: if-elif-else
score = 75
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'
print(f"Your grade: {grade}")

# Practice 3: Multiple conditions with 'and'
temperature = 25
humidity = 60
if temperature > 20 and humidity < 70:
    print("Perfect weather!")

# Practice 4: Multiple conditions with 'or'
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")

# Practice 5: Nested if
marks = 85
attendance = 95
if marks >= 80:
    if attendance >= 90:
        print("Excellent performance!")
    else:
        print("Good marks but improve attendance")
else:
    print("Need to improve marks")


# SECTION 2: LOOPS
# ================

# Practice 6: for loop with range
print("\n--- FOR LOOPS ---")
for i in range(1, 6):  # 1 to 5
    print(f"Number: {i}")

# Practice 7: for loop with range and step
print("\nEven numbers from 2 to 10:")
for i in range(2, 11, 2):  # start, stop, step
    print(i)

# Practice 8: for loop with list
fruits = ["apple", "banana", "orange", "mango"]
for fruit in fruits:
    print(f"I like {fruit}")

# Practice 9: Looping with enumerate (index + value)
print("\nFruits with index:")
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# Practice 10: while loop
print("\n--- WHILE LOOPS ---")
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

# Practice 11: while loop with condition
print("\nGuess a number game:")
secret = 5
guess = 0
while guess != secret:
    guess = int(input("Guess a number (1-10): "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("You got it! Correct answer!")

# Practice 12: break statement
print("\nFind first number divisible by 7:")
for num in range(1, 100):
    if num % 7 == 0:
        print(f"Found: {num}")
        break

# Practice 13: continue statement
print("\nNumbers except multiples of 3:")
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)


# SECTION 3: FUNCTIONS
# ====================

# Practice 14: Simple function
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Practice 15: Function with return value
def add(a, b):
    result = a + b
    return result

sum_result = add(5, 3)
print(f"Sum: {sum_result}")

# Practice 16: Function with multiple parameters
def calculate_area(length, width):
    area = length * width
    return area

area = calculate_area(5, 10)
print(f"Area: {area} square units")

# Practice 17: Function with default parameters
def power(base, exponent=2):
    return base ** exponent

print(f"2^3 = {power(2, 3)}")
print(f"5^2 = {power(5)}")  # uses default

# Practice 18: Function with multiple return values
def get_min_max(numbers):
    return min(numbers), max(numbers)

nums = [3, 7, 2, 9, 1]
min_val, max_val = get_min_max(nums)
print(f"Min: {min_val}, Max: {max_val}")


# SECTION 4: LISTS AND STRINGS
# =============================

# Practice 19: List operations
numbers = [10, 20, 30, 40, 50]
print("\n--- LIST OPERATIONS ---")
print(f"Original list: {numbers}")
numbers.append(60)  # add to end
print(f"After append: {numbers}")
numbers.pop()  # remove last
print(f"After pop: {numbers}")
numbers.insert(2, 25)  # insert at index
print(f"After insert: {numbers}")

# Practice 20: List slicing
print(f"First 3 elements: {numbers[:3]}")
print(f"Last 2 elements: {numbers[-2:]}")
print(f"Every 2nd element: {numbers[::2]}")

# Practice 21: String operations
print("\n--- STRING OPERATIONS ---")
text = "Hello World"
print(f"Original: {text}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Length: {len(text)}")
print(f"Replace: {text.replace('World', 'Python')}")

# Practice 22: String slicing
word = "Python"
print(f"First 3 chars: {word[:3]}")
print(f"Last 2 chars: {word[-2:]}")

# Practice 23: Splitting and joining
sentence = "I love Python programming"
words = sentence.split()
print(f"Words: {words}")
rejoined = " - ".join(words)
print(f"Joined: {rejoined}")


# SECTION 5: COMBINING EVERYTHING
# =================================

# Practice 24: Function with loop and condition
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

text = "Programming is fun"
vowel_count = count_vowels(text)
print(f"\nVowels in '{text}': {vowel_count}")

# Practice 25: List comprehension (bonus)
squares = [x**2 for x in range(1, 6)]
print(f"Squares of 1-5: {squares}")

even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(f"Even numbers 1-20: {even_numbers}")


# ============================================
# CHALLENGES TO TRY
# ============================================
"""
1. Create a function that checks if a number is prime
2. Write a program that prints a multiplication table
3. Create a function to reverse a string
4. Write a program to find the largest number in a list
5. Create a function to check if a word is a palindrome
6. Write a program to calculate factorial of a number
7. Create a function to count occurrences of each character in a string
8. Write a program that simulates a simple calculator
"""
