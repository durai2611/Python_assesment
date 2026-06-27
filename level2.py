#Exercise 1: List Comprehension Mastery
words = ["apple", "bat", "cherry", "dog", "elderberry"]
result = [w.upper() for w in words if len(w) >= 4]
print(result)

#Exercise 7: Palindrome Sentence
sentence = "A man, a plan, a canal: Panama"

# Step 1: Convert to lowercase
sentence = sentence.lower()

# Step 2: Collect valid characters in a list
chars = []
for ch in sentence:
    if ch.isalnum():   # keep only letters and digits
        chars.append(ch)

# Step 3: Join the list into a string
cleaned = "".join(chars)

# Step 4: Check palindrome
print(cleaned == cleaned[::-1])

#Exercise 17: Age Calculator (Exact)
from datetime import date
from dateutil.relativedelta import relativedelta
birthdate = date(1995, 5, 15)
today = date(2026, 1, 2)
age = relativedelta(today, birthdate)
print(f"Age: {age.years} years, {age.months} months, {age.days} days")


