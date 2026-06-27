#Exercise 1: List Comprehension Mastery
words = ["apple", "bat", "cherry", "dog", "elderberry"]
result = [w.upper() for w in words if len(w) >= 4]
print(result)

#Exercise 7: Palindrome Sentence
sentence = "A man, a plan, a canal: Panama"
sentence = sentence.lower()
chars = []
for ch in sentence:
    if ch.isalnum():   
        chars.append(ch)
cleaned = "".join(chars)
print(cleaned == cleaned[::-1])

#Exercise 17: Age Calculator (Exact)
from datetime import date
from dateutil.relativedelta import relativedelta
birthdate = date(1995, 5, 15)
today = date(2026, 1, 2)
age = relativedelta(today, birthdate)
print(f"Age: {age.years} years, {age.months} months, {age.days} days")


