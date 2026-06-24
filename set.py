#Exercise 1: Perform Basic Set Operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A | B)          
print(A.union(B))     
print(A & B)         
print(A.intersection(B))
print(A - B)         
print(A.difference(B))
print(A ^ B)              
print(A.symmetric_difference(B)) 

#Exercise 2: Union of Sets
print(A | B) 

#Exercise 3: Intersection of Sets
print(A & B)  

#Exercise 4: Difference of Sets
print(A - B)         
print(A.difference(B))

#Exercise 5: Symmetric Difference
print(A ^ B)              
print(A.symmetric_difference(B)) 

#Exercise 6: Add a list of Elements to a Set
my_set = {1, 2, 3}
my_list = [3, 4, 5, 6]
my_set.update(my_list)
print(my_set)

#Exercise 7: Set Difference Update
A = {1, 2, 3, 4, 5}
B = {3, 4}
new_set = A.difference(B)
print(new_set)  
print(A)   

#Exercise 8: Remove Items From Set Simultaneously
my_set = {1, 2, 3, 4, 5, 6}
remove_items = {2, 4, 6}
my_set = my_set - remove_items
print(my_set)

#Exercise 9: Check Subset
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
print(A.issubset(B))   
print(B.issubset(A))   

#Exercise 10: Check Superset
print(B.issuperset(A)) 
print(A.issuperset(B)) 

#Exercise 11: Set Intersection Check
if A & B:
    print("Sets intersect")
else:
    print("No intersection")

#Exercise 12: Set Symmetric Difference Update
print(A ^ B)              
print(A.symmetric_difference(B)) 

#Exercise 13: Set Intersection Update
A = {1, 2, 3, 4}
B = {3, 4, 5}
new_set = A.intersection(B)
print(new_set)  
print(A)  

#Exercise 14: Find Common Elements in Two Lists
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
common = A & B
print(common)

#Exercise 15: Frozen Set
fs = frozenset([1, 2, 3, 4])
print(fs)

#Exercise 16: Count Unique Words
text = "apple orange banana apple mango orange apple"
words = text.split()          
unique_words = set(words)     
print(len(unique_words))      
print(unique_words)          











