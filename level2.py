#Exercise 1: List Comprehension Mastery
words = ["apple", "bat", "cherry", "dog", "elderberry"]
result = [w.upper() for w in words if len(w) >= 4]
print(result)

#Exercise 2: Dictionary Merging with Logic
dict_a = {'a': 10, 'b': 20}
dict_b = {'b': 5, 'c': 15}

merged = dict_a.copy()   # start with dict_a
for key, value in dict_b.items():
    merged[key] = merged.get(key, 0) + value
print("Merged Dictionary:", merged)

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

#




