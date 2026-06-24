#Exercise 1: Perform basic dictionary operations
my_dict = {"name": "durai", "age": 33, "city": "Bangalore"}
print(my_dict["name"])       
print(my_dict.get("age"))    

#Exercise 2: Perform dictionary operations

# Create a dictionary
my_dict = {"name": "durai", "age": 33, "city": "Bangalore"}

# Access values
print("Name:", my_dict["name"])          
print("Age:", my_dict["age"])        

# Add or update values
my_dict["age"] = 34                     
my_dict["profession"] = "Engineer"       
print("Updated dict:", my_dict)

# Remove values
my_dict.pop("city")                      
del my_dict["name"]                      
print("After removals:", my_dict)

# Iterate over dictionary
for key, value in my_dict.items():
    print(key, ":", value)

# Dictionary methods
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())

# Merge/update with another dictionary
my_dict.update({"country": "India", "age": 34})
print("After update:", my_dict)

#Exercise 3: Dictionary from Lists
keys = ["name", "age", "city"]
values = ["durai", 33, "Bengaluru"]
my_dict = dict(zip(keys, values))
print(my_dict)

#Exercise 4: Clear Dictionary
my_dict = {"name": "durai", "age": 33, "city": "Bangalore"}
my_dict.clear()
print(my_dict)

#Exercise 5: Merge two Python dictionaries into one
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(dict1)  

#method2
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2
print(merged) 

#Exercise 6: Count Character Frequencies
freq_dict={"durai"}
from collections import Counter
freq_dict = dict(Counter("durai"))
print(freq_dict)

#Exercise 7: Access Nested Dictionary
student = {
    "name": "durai",
    "details": {
        "age": 25,
        "city": "bangalore",
        "marks": {
            "math": 90,
            "science": 85
        }
    }
}
print(student.get("details").get("marks"))

#Exercise 8: Print the value of key ‘history’ from nested dictionary
student = {
    "name": "durai",
    "details": {
        "age": 34,
        "city": "bengalore",
        "marks": {
            "math": 90,
            "science": 85,
            "history": 88
        }
    }
}
print(student["details"]["marks"]["history"])
#Exercise 9: Modify Nested Dictionary
student["details"]["marks"]["science"] = 95
print(student["details"]["marks"])

#Exercise 10: Initialize dictionary with default values
keys = ["math", "science", "history"]
my_dict = {key: 0 for key in keys}
print(my_dict)

#Exercise 11: Create a dictionary by extracting the keys from a given dictionary
student = {"name": "durai", "age": 33, "city": "Bangalore"}
keys_to_extract = ["name", "age"]
new_dict = {key: student[key] for key in keys_to_extract}
print(new_dict)

#Exercise 12: Delete a list of keys from a dictionary
student = {"name": "durai", "age": 33, "city": "Bangalore"}
keys_to_delete = ["age", "city"]
for key in keys_to_delete:
    student.pop(key)  
print(student)

#Exercise 13: Check if a value exists in a dictionary
print("durai" in student.values())   
print(33 in student.values()) 

#Exercise 14: Rename key of a dictionary
student["years"] = student.pop("age")
print(student)

#Exercise 15: Get the key of a minimum value
student = {"math": 90, "science": 85, "history": 70, "english": 88}
min_key = min(student, key=student.get)
print(min_key)

#Exercise 16: Change value of a key in a nested dictionary
student = {
    "name": "durai",
    "details": {
        "age": 34,
        "city": "bengalore",
        "marks": {
            "math": 90,
            "science": 85,
            "history": 88
        }
    }
}
student["details"]["marks"]["science"] = 95
print(student["details"]["marks"])

#Exercise 17:Inverted dictionary
student = {"math": 90, "science": 85, "history": 70, "english": 88}
inverted = dict(zip(student.values(), student.keys()))
print(inverted)

#Exercise 18: Sort Dictionary by Keys
sorted_dict = dict(sorted(student.items()))
print(sorted_dict)

#Exercise 19: Sort Dictionary by Values
student = {"math": 90, "science": 85, "history": 70, "english": 88}
sorted_dict = {k: student[k] for k in sorted(student, key=student.get)}
print(sorted_dict)

#Exercise 20: Check if All Values are Unique
values = student.values()
is_unique = len(values) == len(set(values))
print(is_unique)  














