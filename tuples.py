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


