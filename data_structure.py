# Q1.Discuss string slicing and provide examples?
# Ans-Slicing in python refers to extracting specific portions  of a string using
# indices. Slicing string Python involves obtaining a sub-string from a given string by slicing it
# from start to end.
# Using Index positions, slicing allows you to capture substrings or characters with the slice
# syntax.
# Syntax-: String[start : end : step ]
# Step by default is 1
# Example
str = "Hello World"
print(str[1:4]) # o/p->"ell"





# Q2.Explain the key features of lists in Python?
# Ans.Features of List in python -:
# 1-Ordered-Lists maintain the order of elements. When you add elements to a list, they are stored in a specific sequence.
# 2-Mutable-Lists are mutable, meaning you can modify them after creation.
# 3-Heterogeneous Elements-A list can contain elements of different data types.We can store integers, strings, floats, and even other lists or complex objects together.
# 4-Indexed Access-Each element in a list is assigned an index, starting from 0 for the first element, 1 for the second, and so on. You can use these indices to access  elements.
# 5-Dynamic Size-Lists in Python can dynamically grow or shrink. You can append or remove items without worrying about the initial size.
# Example -:
li = [1,2,3,4,5]
print(li[0]) # o/p-> 1
print(type(li)) # o/p-> 'list'






# Q3.Describe how to access, modify  and delete elements in a list with examples.
#  List are used to store multiple items in a single variable.Accessing, modifying, and deleting elements in a Python list are common operations.
#  1-Accessing Elements - We can access elements in a list using indexing and slicing.
li1 = [1,2,3,4,5]
print(li1[0]) # o/p-> 1
print(li1[-1]) # o/p-> 5
print(li1[1:4]) # o/p-> [2,3,4]
# 2-Modifying Elements-We can modify elements by assigning a new value to a specific index or range of indices.
li_m = [1,2,3,4,5]
li_m[0] = "Helo"
li_m[-1] = 55
print(li_m) #o/p-> ['Helo', 2, 3, 4, 55]
# Deleting Elements - We can delete elements using del, remove(), or pop().
li_d = [4,2,52,5,78]
li_d.remove(4) # o/p -> remove 2
li_d.pop(2) #o/p remove 5
print(li_d) #o/p -> [2,52,78]





#  Q4.Compare and contrast tuples and list with examples
#Tuples:
# 1- Tuples are immutable , it means elements can not be change after once created.
# 2- The implication of iteration is comparatively Faster
# 3- A Tuple data type is appropriate for accessing the elements
# 4- Tuple consumes less memory as compared to the list
my_tuple=("ram",1.2,"sita",4,5,True,3+5j)
print(my_tuple)
#my_tuple[0] = "gita" # error
print(my_tuple.count(1))  # o/p: 1
print(my_tuple.index(3))  # o/p: 2

# Lists:
# 1- List are mutable,it means elements can be changed after once created.
# 2- The implication of iteration is time-consuming.
# 3- The list is better for performing operation,such as insertion and deletion
# 4- List consume more memory.
list_a = [1, 2, 3]
list_b = list_a.copy()
list_b[0] = 10
print(list_a)  # o/p: [1, 2, 3] (original list)
print(list_b)  # o/p: [10, 2, 3] (copied and modified)






# Q5-Describe the key features of sets and provide examples of their use.
# In Python, a set is an unordered collection of unique elements. It is particularly useful when you want to store distinct
# items and perform operations like union, intersection, and difference.
# Key Features of Sets-:
# 1- Unordered -A set is an unordered collection, meaning the elements have no defined order and cannot be accessed by an index.
my_set = {3, 1, 4, 2}
print(my_set)  # Output: {1, 2, 3, 4} (order may vary)
# 2-  Unique Elements -Sets automatically eliminate duplicates. If you try to add a duplicate element, it will not be included in the set.
my_set = {1, 2, 2, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4} (duplicates removed)
# 3- Mutable - Sets are mutable, meaning you can add or remove elements after the set is created.
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}
# 4- . No Indexing or Slicing - Since sets are unordered, you cannot access elements via indexing or slicing (unlike lists or tuples).
my_set = {1, 2, 3}
# print(my_set[0])  # This will raise a TypeError because sets don't support indexing.
# 5- Set Operations - Sets support mathematical set operations like union, intersection, difference, and symmetric difference.
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union: Combine both sets (removes duplicates)
print(set_a | set_b)  # Output: {1, 2, 3, 4, 5}

# Intersection: Common elements in both sets
print(set_a & set_b)  # Output: {3}

# Difference: Elements in set_a but not in set_b
print(set_a - set_b)  # Output: {1, 2}

# Symmetric Difference: Elements in either set, but not both
print(set_a ^ set_b)  # Output: {1, 2, 4, 5}






# Q6- Discuss the use cases of tuples and sets in python programming
# Use cases for Tuples -:
# 1- Storing fixed data like geographical coordinates, RGB color values, etc.
# 2- Use tuples in performance-critical sections of the code where you need to iterate over large collections of constant data.
# 3- Passing tuples as function arguments to ensure that the data passed to the function cannot be changed inside the function.
# 4- Returning multiple values from a function in a structured format.
# 5- Use a tuple to represent an entity with different types of information (e.g., a record from a database, where each field might be a different data type).

# Use cases of Sets-:
# 1- Removing duplicates from a list.
# 2- Checking membership in a large dataset or filtering data based on membership.
# 3- Finding common elements between two collections or identifying differences.
# 4- Cleaning up data from a file or database by removing duplicate entries.
# 5- Tracking seen elements while processing streams of data.




#  Q7.Describe how to add, modify, and delete items in a dictionary with examples
#  Dictionary:- These are used to store data value in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicate.
#  Example:
A={"Math":99,"English":99,"Hindi":98,"Science":98,"Social Science":97}
print(A)
#  Dictionary-item: Dictionary item are ordered,changeable,and do not allow duplicate
#  Dictionary items are presented in key:value pairs , and can be referred to by using the key name.
#  Example:
A={"Math":99,"English":99,"Hindi":98,"Science":98,"Social Science":97}
print(A["Math"])
#  Adding items : Adding an item to the dictionary is done by using a new index key and
#  assigning a value to it.
#  Example:
A={"Math":99,"English":99,"Hindi":98,"Science":98,"Social Science":97}
A["Drawing"]=99
print(A)
#  Change Dictionary Items:
#  Change Value: you can change the value of a specific item by referring to its key name
#  Example:
A={"Math":99,"English":99,"Hindi":98,"Science":98,"Social Science":97}
A["Math"]=75
print(A)
#  Update Dictionary:
#  The update() method will update the dictionary with the items from the given argument.
#  The argument must be a dictionary ,or an iterable object with key:value pairs.
#  Example:
A={"Math":99,"English":99,"Hindi":98,"Science":98,"Social Science":97}
A.update({"Science":57})
print(A)
#  Get Keys:- The keys() method will return a list of all the keys in the dictionary.
#  Example:
A={"Math":99,"English":99,"Hindi":98,"Science":98,"Social Science":97}
print(A.keys())
#  Get Values:
#  The values() method will return a list of all the values in the dictionary.
#  Example:
A={"Math":99,"English":99,"Hindi":98,"Science":98,"Social Science":97}
print(A.values())
#  Get items: items() method will return each item in a dictionary , as tuples in a list.
#  Example:
A={"Math":99,"English":99,"Hindi":98,"Science":98,"Social Science":97}
A.items()
#  Remove items:
#  pop() method to remove items from a dictionary.pop() takes a key as an input and deletes the corresponding item from the python dictionary. It returns the values associated with input key.
#  Example:
A={"Math":99,"English":99,"Hindi":98,"Science":98,"Social Science":97}
A.pop("Social Science")
print(A)
#  popItem() : removes and returns a random item key-value from the dictionary.
#  Example:
A={"Math":99,"English":99,"Hindi":98,"Science":98,"Social Science":97}
A.popitem()
print(A)
#  clear():- This method drops all the items from the dictionary.clear() is referred to as the flush method because it flushes everything from the dictionary.
#  Example:
A={"Math":99,"English":99,"Hindi":98,"Science":98,"Social Science":97}
A.clear()
print(A)
#  del:- Another way to remove an element from a dictionary is to use the del keyword del deletes individual elements and eventually the entire dictionary object.
#  Example:
A={"Math":99,"English":99,"Hindi":98,"Science":98,"Social Science":97}
del A






# 8.Discuss the importance of dictionary keys being immutable and provide examples.
#  Ans. Dictionaries store key-value pairs: Keys are analogous to indexes of a list.When using list you access the element via the index .With dictionaries you access value via the
#  Keys.The keys can be of any datatype.
#  Why must dictionaries keys be immutable:
#  The hash table implementation of dictionaries uses a hash value calculated from the
#  ley value to find the key.
#  If the key were a mutable object , its value could change,and thus its hash could also
#  change.
#  The Python dictionary keys() function can be used to access dictionary elements in the same way that we can access list elements,however ,without the usages of keys(), no other
#  mechanism provides a way to access dictionary keys as a list by index.
#  Retrieving dictionary keys as a list can be useful in many scenarios. It allows you to perform operations on the keys , such as iterating over them, checking for the presence of a specific
#  key or performing operation based on the key’s values.By converting the keys into a list, you can easily manipulate and analyse the data within the dictionary.
A = {"Math": [99, 45, 44]}
print(A["Math"][1])
a = {["Math", "Eng", "hindi"]: 95}
print(a)










