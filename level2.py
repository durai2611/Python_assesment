#Exercise 1: List Comprehension Mastery
words = ["apple", "bat", "cherry", "dog", "elderberry"]
result = [w.upper() for w in words if len(w) >= 4]
print(result)

#Exercise 2: Dictionary Merging with Logic
dict_a = {'a': 10, 'b': 20}
dict_b = {'b': 5, 'c': 15}
merged = dict_a | dict_b
print(merged)

#Exercise 3: Frequency Map with Counter
from collections import Counter
text = "Python Programming"
text = text.lower()
text = text.replace(" ", "")
frequency = Counter(text)
print("Character Frequency:", frequency)

#Exercise 4: Anagram Checker
def are_anagrams(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2)
word1 = "listen"
word2 = "silent"
print(f'Is "{word1}" an anagram of "{word2}"? {are_anagrams(word1, word2)}')

#Exercise 5: Flatten a Nested List
def flatten_list(nested):
    flat = []
    for item in nested:
        if isinstance(item, list):   # if the element is a list, recurse
            flat.extend(flatten_list(item))
        else:                        # if not a list, just add it
            flat.append(item)
    return flat
nested = [1, [2, 3], [4, [5, 6]], 7]
result = flatten_list(nested)
print("Flattened:", result)

#Exercise 6: Reverse Each Word of a String
sentence = "Python is awesome"
reversed_sentence = " ".join([word[::-1] for word in sentence.split()])
print(reversed_sentence)  

#Exercise 7: Palindrome Sentence
sentence = "A man, a plan, a canal: Panama"
sentence = sentence.lower()
chars = []
for ch in sentence:
    if ch.isalnum():   
        chars.append(ch)
cleaned = "".join(chars)
print(cleaned == cleaned[::-1])

#Exercise 8: List Comprehension Filtering (Advanced)

strings = ["apple", "education", "ice", "ocean", "python", "umbrella"]
result = [word for word in strings if len(word) > 5 and word[0].lower() in 'aeiou']
print(result)  # Output: ['education', 'umbrella']

#Exercise 9: Remove Duplicates (Preserving Order)
def remove_duplicates(lst):
    seen = []
    for item in lst:
        if item not in seen:
            seen.append(item)
    return seen
input_list = [1, 2, 2, 3, 1, 4, 2]
output_list = remove_duplicates(input_list)
print(output_list)  # Output: [1, 2, 3, 4]

#Exercise 10: Circular Shift (Rotation)
def rotate_list(lst, n, direction):
    n = n % len(lst)  # Handle cases where n > length of list
    if direction == 'right':
        return lst[-n:] + lst[:-n]
    elif direction == 'left':
        return lst[n:] + lst[:n]
    else:
        raise ValueError("Direction must be 'left' or 'right'")
input_list = [1, 2, 3, 4, 5]
shift = 2
direction = 'right'
output_list = rotate_list(input_list, shift, direction)
print(output_list)  # Output: [4, 5, 1, 2, 3]

#Exercise 11: Dictionary Merging (Value Grouping)
def merge_dicts(d1, d2):
    merged = {}
    for key in set(d1.keys()).union(d2.keys()):
        values = []
        if key in d1:
            values.append(d1[key])
        if key in d2:
            values.append(d2[key])
        merged[key] = values
    return merged
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
result = merge_dicts(d1, d2)
print(result)  # Output: {'a': [1], 'b': [2, 3], 'c': [4]}

#Exercise 12: Inverted Index
def invert_dict(author_books):
    inverted = {}
    for author, books in author_books.items():
        for book in books:
            inverted[book] = author
    return inverted
authors = {"Orwell": ["1984", "Animal Farm"], "Huxley": ["Brave New World"]}
books = invert_dict(authors)
print(books)

#Exercise 13: Dictionary Sorting (Lambda)
employees = [
    {"name": "A", "salary": 50},
    {"name": "B", "salary": 70},
    {"name": "C", "salary": 60}
]
sorted_employees = sorted(employees, key=lambda x: x["salary"], reverse=True)
print(sorted_employees)

#Exercise 14: Subset and Superset Validation
# Input lists
list_a = [1, 2, 3]
list_b = [1, 2, 3, 4, 5]
set_a = set(list_a)
set_b = set(list_b)
if set_a.issubset(set_b):
    print("Set A is a subset of Set B.")
elif set_a.issuperset(set_b):
    print("Set A is a superset of Set B.")
elif set_a.isdisjoint(set_b):
    print("Set A is disjoint from Set B.")
else:
    print("Sets have some overlap but are not subset/superset.")

#Exercise 15: Set Symmetric Difference
list1 = [101, 102, 103]
list2 = [103, 104, 105]
set1 = set(list1)
set2 = set(list2)
result = set1 ^ set2
print(result)  

#Exercise 16: Power Set Generation
from itertools import chain, combinations

def power_set(lst):
    return list(chain.from_iterable(combinations(lst, r) for r in range(len(lst)+1)))
input_list = [1, 2, 3]
output = power_set(input_list)
print(output)

#Exercise 17: Age Calculator (Exact)
from datetime import date
from dateutil.relativedelta import relativedelta
birthdate = date(1995, 5, 15)
today = date(2026, 1, 2)
age = relativedelta(today, birthdate)
print(f"Age: {age.years} years, {age.months} months, {age.days} days")

#Exercise 18: Countdown Timer (Time Delta)
from datetime import datetime, timedelta

def time_until_new_year(current_date_str):
    # Parse the current date string
    current_date = datetime.strptime(current_date_str, "%Y-%m-%d")
    
    # Define upcoming New Year's Day (Jan 1 of the next year)
    new_year = datetime(year=current_date.year + 1, month=1, day=1)
    
    # Calculate the difference
    delta = new_year - current_date
    
    # Extract days, hours, minutes
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    
    return f"{days} days, {hours} hours, {minutes} minutes until New Year!"
print(time_until_new_year("2026-01-02"))

#Exercise 19: Business Days Calculator
from datetime import datetime, timedelta

def add_business_days(start_date_str, n):
    # Parse the start date string
    current_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    
    days_added = 0
    while days_added < n:
        current_date += timedelta(days=1)
        if current_date.weekday() < 5:
            days_added += 1
    return current_date.strftime("%Y-%m-%d")
start = "2026-01-02"  
n = 5
result = add_business_days(start, n)
print(result) 

#Exercise 20: Custom Iterator Class
class PowerOfTwo:
    def __init__(self, max_exponent):
        self.max_exponent = max_exponent
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_exponent:
            raise StopIteration
        result = 2 ** self.current
        self.current += 1
        return result
powers = PowerOfTwo(3)
for value in powers:
    print(value)

#Exercise 21: Find Duplicates in O(n) Time
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    
    for num in lst:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return duplicates
numbers = [1, 2, 3, 2, 4, 5, 1, 6]
result = find_duplicates(numbers)
print("Duplicates found:", result)

#Exercise 22: Singly Linked List Implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:  # If list is empty
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()

#Exercise 23: Stack Implementation (LIFO)
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

stack = Stack()
stack.push("google.com")
stack.push("pynative.com")

print("Current Top:", stack.peek())   
popped = stack.pop()
print("Popped:", popped)             
print("New Top:", stack.peek())      

#Exercise 24: Queue Implementation (FIFO)
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0
queue = Queue()
queue.enqueue("Customer A")
queue.enqueue("Customer B")

serving = queue.dequeue()
print("Serving:", serving)             
print("Next in line:", queue.peek())   

#Exercise 25: Recursive Binary Search
def binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    # Base case: target not found
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)


# Example usage
sorted_list = [10, 20, 30, 40, 50, 60]
target = 50

index = binary_search(sorted_list, target)
if index != -1:
    print(f"Target found at index: {index}")
else:
    print("Target not found")

#Exercise 26: Lambda Sorting with Tuples
employees = [("Alice", 30, 50000), 
             ("Bob", 25, 75000), 
             ("Charlie", 35, 60000)]

# Sort primarily by Salary (index 2) in descending order
sorted_employees = sorted(employees, key=lambda x: x[2], reverse=True)

print(sorted_employees)

#Exercise 27: Map and Filter Combination
nums = [1, 2, 3, 4, 5, 6]
squares_of_evens = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
print(squares_of_evens)

#Exercise 28: Custom @timer Decorator
import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function '{func.__name__}' took {end - start:.4f} seconds to run.")
        return result
    return wrapper

@timer
def waste_time():
    time.sleep(1.5)  # Simulate heavy computation

# Example usage
waste_time()

#Exercise 29: Fibonacci Generator (Memory Efficiency)   
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

n = 8
print(f"First {n} Fibonacci numbers:", end=" ")
for num in fibonacci(n):
    print(num, end=" ")

#Exercise 30: Custom Context Manager ( with statement)
class DatabaseConnection:
    def __enter__(self):
        print("Connecting to Database...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"Error: {exc_value}")
        print("Closing Database Connection safely.")
        # Returning False ensures exceptions are not suppressed
        return False

try:
    with DatabaseConnection() as conn:
        print("Processing data...")
        # Simulate an error
        raise Exception("something went wrong")
except Exception:
    pass
#Exercise 31: The Versatile *args and **kwargs
def log_event(message, *args, **kwargs):
    print(f"Event: {message}")
    if args:
        print(f"Details: {args}")
    if kwargs:
        print(f"Metadata: {kwargs}")
log_event("User Login", "admin", "dashboard", timestamp="10:00 AM", status="Success")

#Exercise 32: Zip and Enumerate Mapping
names = ["durai", "varun", "rajan"]
scores = [85, 92, 78]

# Combine into dictionary
student_scores = dict(zip(names, scores))

# Sort by score in descending order
sorted_students = sorted(student_scores.items(), key=lambda x: x[1], reverse=True)

# Print ranked list using enumerate
for rank, (name, score) in enumerate(sorted_students, start=1):
    print(f"Rank {rank}: {name} scored {score}")

#Exercise 33: Memoization with lru_cache
import functools
@functools.lru_cache(maxsize=None)
def fibonacci(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
result = fibonacci(50)
print(f"Fibonacci(50) = {result}")

#Exercise 34: Set Operations for Data Analysis
trial = [1, 2, 3, 4, 5]
paid = [4, 5, 6, 7, 8]

# Convert to sets
trial_set = set(trial)
paid_set = set(paid)

# Find upgraded (both trial and paid)
upgraded = trial_set & paid_set

# Find leads (trial only)
leads = trial_set - paid_set

# Find unique status (not both)
unique_status = trial_set ^ paid_set

print("Upgraded (Both):", upgraded)
print("Leads (Trial only):", leads)
print("Unique Status (Not both):", unique_status)

#Exercise 35: Inheritance and Method Overriding
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def fuel_type(self):
        return "Generic Fuel"

class ElectricCar(Vehicle):
    def fuel_type(self):
        return "Electricity"

# Example usage
car = ElectricCar("Tesla")
print(f"Brand: {car.brand}")
print(f"Fuel Type: {car.fuel_type()}")

#Exercise 36: Encapsulation (Private Attributes)
class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.__balance}")

    def get_balance(self):
        return self.__balance
account = BankAccount(100)
account.deposit(50)
account.withdraw(200)  # triggers warning
print("Final Balance:", account.get_balance())

#Exercise 37: Property Decorators ( @property )
class Student:
    def __init__(self, name):
        self.name = name
        self.__score = 0  # private attribute

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self.__score = value
        else:
            raise ValueError("Score must be between 0 and 100.")

s = Student("durai")
s.score = 105  

#Exercise 38: Class Methods vs. Static Methods
class Pizza:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def margherita(cls):
        # Pre-configured Pizza object
        return cls("Margherita", 8.99)

    @staticmethod
    def validate_topping(topping):
        healthy_toppings = {"tomato", "spinach", "mushroom", "pineapple"}
        return topping.lower() in healthy_toppings

my_pizza = Pizza.margherita()
print(f"Pizza ordered: {my_pizza.name}")

is_valid = Pizza.validate_topping("pineapple")
print("Is topping valid?", is_valid)

#Exercise 39: Magic Methods ( __str__ and __add__ )
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2) 

#Exercise 40: Abstract Base Classes (ABC)
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

shapes = [Circle(5), Square(4)]

for shape in shapes:
    if isinstance(shape, Circle):
        print(f"Circle Area: {shape.area():.2f}")
    elif isinstance(shape, Square):
        print(f"Square Area: {shape.area()}")

#Exercise 41: Multiple Inheritance and MRO
class Flyer:
    def fly(self):
        print("Flying high!")

class Swimmer:
    def swim(self):
        print("Swimming fast!")

class Duck(Flyer, Swimmer):
    pass

# Example usage
d = Duck()
d.fly()
d.swim()
print("MRO:", Duck.__mro__)

#Exercise 42: Composition over Inheritance
class CPU:
    def __init__(self, model):
        self.model = model

class RAM:
    def __init__(self, size):
        self.size = size

class Computer:
    def __init__(self, cpu_model, ram_size):
        # Composition: Computer has-a CPU and has-a RAM
        self.cpu = CPU(cpu_model)
        self.ram = RAM(ram_size)

    def __str__(self):
        return f"Computer with {self.cpu.model} CPU and {self.ram.size} RAM."

my_comp = Computer("Intel i7", "16GB")
print(my_comp)

#Exercise 43: The Singleton Pattern
class Database:
    _instance = None  # class-level attribute to store the single instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Loading Database...")
            cls._instance = super().__new__(cls)
        return cls._instance
db1 = Database()
db2 = Database()
print(db1 is db2)  # True → both point to the same object

#Exercise 44: Data Classes ( @dataclass )
from dataclasses import dataclass
@dataclass
class Book:
    title: str
    author: str
    pages: int
b1 = Book("1984", "George Orwell", 328)
print(b1)

#Exercise 53: Student Management System
# Dictionary to hold student records
students = {}

def add_student(student_id, name, grade):
    students[student_id] = {"Name": name, "Grade": grade}

def update_grade(student_id, new_grade):
    if student_id in students:
        students[student_id]["Grade"] = new_grade
    else:
        print(f"Student ID {student_id} not found.")

def display_all():
    for sid, info in students.items():
        print(f"ID: {sid} | Name: {info['Name']} | Grade: {info['Grade']}")
add_student(101, "Alice", "A")
update_grade(101, "A+")
display_all()

#Exercise 54: Password Strength Checker
import string

def strength_score(password):
    score = 0
    
    # Criteria checks
    if len(password) >= 8:
        score += 1
    if any(ch.isupper() for ch in password):
        score += 1
    if any(ch.islower() for ch in password):
        score += 1
    if any(ch.isdigit() for ch in password):
        score += 1
    if any(ch in string.punctuation for ch in password):
        score += 1

    descriptions = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Good",
        4: "Strong",
        5: "Very Strong"
    }
    
    return f"Strength: {score}/5 ({descriptions[score]})"
print(strength_score("P@ss123"))

#Exercise 55: Number Guessing Game (Computer vs User)
import random

def number_guessing_game():
    target = random.randint(1, 100)
    attempts = 10
    print("I'm thinking of a number between 1 and 100.")

    while attempts > 0:
        print(f"({attempts} left)")
        guess = int(input("Enter guess: "))

        if guess == target:
            print(f"Correct! The number was {target}.")
            break
        elif guess < target:
            print("Higher!")
        else:
            print("Lower!")

        attempts -= 1

    if attempts == 0:
        print(f"Out of attempts! The number was {target}.")
number_guessing_game()

#Exercise 56: File Word Count Tool
# Open the file in read mode
f = open("sample.txt", "r")
data = f.read()
f.close()
lines = data.splitlines()
words = data.split()
characters = len(data)
print("Lines:", len(lines), "| Words:", len(words), "| Characters:", characters)

#Exercise 57: Prime Number Generator
import math

def primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num < 2:
            continue
        is_prime = True
        # Only check divisors up to sqrt(num)
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
print("Primes:", primes_in_range(10, 50))

#
#Exercise 66: Find the second largest number
# Input list
numbers = [1, 2, 3, 4, 5]

# Remove duplicates and sort
numbers = sorted(set(numbers))

# Print the second largest
print(numbers[-2])

#Exercise 67: Print numbers in reverse order using function recursive method
def print_reverse(n):
    if n < 0:
        return
    print(n, end=" ")
    print_reverse(n - 1)

print_reverse(10)


#Exercise 68: Print Fibonacci series in recursive method
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Print first 9 Fibonacci numbers
for i in range(9):
    print(fibonacci(i), end=",")





















