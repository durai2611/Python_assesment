#Exercise 1: Perform Basic Tuple Operations
t = (10, 20, 30, 40, 50)
print(t[0])   
print(t[-1])  
t2 = (60, 70)
print(t + t2) 
print(t * 2)  

#Exercise 2: Tuple Repetition
print(t * 3)  

#Exercise 3:Slicing Tuples
print(t[0])   
print(t[-3]) 

#Exercise 4: Reverse the tuple
reversed_t = t[::-1]
print(reversed_t)

#Exercise 5: Access Nested Tuples
nested_t = ((1, 2, 3), (4, 5, 6), (7, 8))
print(nested_t[0])   # (1, 2, 3)
print(nested_t[1])   # (4, 5, 6)
print(nested_t[2])   # (7, 8)
print(nested_t[0][1])   # 2
print(nested_t[1][2])   # 6
print(nested_t[2][0])   # 7

#Exercise 6: Create a tuple with single item 50
t = (50,)
print(t)

# Exercise 7: Unpack the tuple into 4 variables
t=(10,20,30,40)
a, b, c, d = t
print(a)  # 10
print(b)  # 20
print(c)  # 30
print(d)  # 40

#Exercise 8: Swap two tuples in Python
t1 = (10, 20, 30)
t2 = (40, 50, 60)
print("t1:", t1)   
print("t2:", t2)   

#Exercise 9: Copy Specific Elements From Tuple
selected = (t[0], t[2], t[5])
print(selected)   

#Exercise 10: List to Tuple
my_list = [10, 20, 30, 40]
my_tuple = tuple(my_list)
print(my_tuple)

#Exercise 11: Function Returning Tuple
def calculate(a, b):
    sum_val = a + b
    diff_val = a - b
    prod_val = a * b
    return (sum_val, diff_val, prod_val)
result = calculate(10, 5)
print(result) 

#Exercise 12: Comparing Tuples
t1 = (10, 20, 30)
t2 = (10, 25, 30)
t3 = (10, 20, 30)
print(t1 == t3)   
print(t1 == t2)   

#Exercise 13: Removing Duplicates from Tuple
t = (10, 20, 30, 20, 40, 10)
unique_t = tuple(set(t))
print(unique_t)

#Exercise 14: Filter Tuples
filtered = tuple(x for x in t if x % 2 == 0)
print(filtered)

#Exercise 15: Map Tuples
t = ("apple", "banana", "cherry")
lengths = tuple(map(len, t))
print(lengths)
# (5, 6, 6)

#Exercise 16: Modify Tuple
lst = list(t)
lst[1] = 99   # change second element
t = tuple(lst)
print(t)

#Exercise 17: Sort a tuple of tuples by 2nd item
data = ((1, 4), (2, 3), (3, 2), (4, 1))
sorted_data = tuple(sorted(data, key=lambda x: x[1]))
print(sorted_data)

#Exercise 18: Count Elements
t = (10, 20, 30, 20, 40, 10, 20)
print(len(t))  

#Exercise 19: Check if all items in the tuple are the same
result = len(set(t)) == 1
print(result)   











