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
