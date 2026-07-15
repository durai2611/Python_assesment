#Exercise1: Basic List Operations
numbers = [1, 2, 3, 6, 8, 9, 4, 5]
numbers.append(6)
print(numbers)
#insert
numbers.insert(2, 99)
print(numbers) 
#remove
numbers.remove(99)
print(numbers)  
#checking numbers in list
print(4 in numbers)  
print(10 in numbers)  
#sorting
numbers.sort()
print(numbers)  
#reversing
numbers.reverse()
print(numbers) 

#Exercise 2: List manipulation
numbers = [1, 2, 2, 3, 4, 5]
print(min(numbers))  
print(max(numbers))  

# remove duplicate
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(numbers))
print(unique) 

#Exercise 3: Sum and average of all numbers in a list
numbers = [1, 2, 2, 3, 4, 4, 5]
total = sum(numbers)
print("Sum of numbers:", total)

#Exercise 4:
list1 = [1, 2, 2, 3, 4, 5]
list_reverse=list1[ ::-1]
print(list_reverse)

#Excercise 5:
numbers = [1, 2, 2, 3, 4, 4, 5]
squares = []
for num in numbers:
    squares.append(num**2)
print("Squares:", squares)

#Exercise 6: Find Maximum and Minimum
numbers = [1, 2, 2, 3, 4, 5]
print(min(numbers))  
print(max(numbers))

#Exercise 7:Count Occurrences
numbers = [1, 2, 2, 3, 4, 5]
count_2 = numbers.count(2)
print("Occurrences of 2:", count_2)

#Excercise 8: Sort a list of numbers
numbers = [1, 2, 2, 3, 4, 5]
numbers.sort()
print(numbers) 

#Exercise 9: Create a copy of a list
list1 = [1, 2, 2, 3, 4, 5]
list_copy=list1[:]
print(list_copy)

#Exercise 10: Combine two lists
List1= [1, 2, 2, 3, 4, 5]
List2= [7,45,5,5]
combined = List1 + List2
print("Combined list:", combined)

#Exercise 11: Remove empty strings from the list of strings
strings = ["apple", "", "banana", "", "cherry", ""]
filtered = []
for s in strings:
    if s != "":
        filtered.append(s)
print(filtered)

#Exercise 12: Remove Duplicates from list
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(numbers))
print(unique) 

#Exercise 13: Remove all occurrences of a specific item from a list
numbers = [1, 2, 2, 3, 4, 2, 5]
filtered = []
for num in numbers:
    if num != 3:
        filtered.append(num)
print(filtered)

#Exercise 14: List Comprehension for Numbers
numbers = [1, 2, 3, 4, 5, 6]
evens = [x**2 for x in numbers if x % 2 == 0]
print(evens)

#Exercise 15: Access Nested Lists
nested = [[1, 2, 3], [4, 5, 6], [7, [8, 9, 10]]]
print(nested[1][2])
print(nested[2][1][0])

#Exercise 16: Flatten Nested List
nested_list = [[1, 2, 3], [4, 5, 6], [7, [8, 9, 10]]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list) 

#Exercise 17: Concatenate two lists index-wise
list1 = ["a", "b", "c"]
list2 = ["1", "2", "3"]
result = [i + j for i, j in zip(list1, list2)]
print(result) 

#Exercise 18: Concatenate two lists in the following order
list1 = ["a", "b", "c"]
list2 = ["1", "2", "3"]
result = [elem for pair in zip(list1, list2) for elem in pair]
print(result)  # ['a', '1', 'b', '2', 'c', '3']

#Exercise 19: Iterate both lists simultaneously
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x, y in zip(list1, list2):
    print(x, y)

#Exercise 20: Add new item to list after a specified item
my_list = ["a", "b", "c", "d"]
my_list.insert(2,"x")
print(my_list)

#Exercise 21: Extend nested list by adding the sublist
nested_list = [[1, 2], [3, 4]]
sublist = [5, 6]
nested_list.extend([sublist])
print(nested_list)  # [[1, 2], [3, 4], [5, 6]]

#Exercise 22: Replace list’s item with new value if found
list1 = ["a", "b", "c"]
list1[list1.index("a")] = "b"
print(list1)  





