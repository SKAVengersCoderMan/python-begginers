"""
More on lists!

sort(): Sorts the list in ascending order.
type(list): It returns the class type of an object.
append(): Adds a single element to a list.
extend(): Adds multiple elements to a list.
index(): Returns the first appearance of the specified value.
max(list): It returns an item from the list with max value.
min(list): It returns an item from the list with min value.
len(list): It gives the total length of the list.
list(seq): Converts a tuple into a list.

Thank you datacamp.com for the documentation. Link for their website in the desciption!

"""

# This is the main list!
our_list = [3, 1, 7, 19, 11, 16, 9]

# sort() helps arrange objects(items) in ascending order.
print(our_list, "\n\n")
our_list.sort()
print(our_list, "\n\n")

# type() tells us what type of data type is our list. The 4 main data types are lists, tuples, sets and dictionaries.
a = type(our_list)
print(a, "\n\n")

# append() and extend() add items in a list
our_list.append(8)
our_list.extend([0])
print(our_list, "\n\n")

# index() return the indexing value of a item in a list.
b = our_list.index(3)
print(b, "\n\n")

# max() returns the largest value of the list.
c = max(our_list)
print(c, "\n\n")

# min() returns the lowest value of the list.
d = min(our_list)
print(d, "\n\n")

# len() returns the lenght of a list.
e = len(our_list)
print(e, "\n\n")

# list() converts a tuple to a list.
tuples_ = (1,2,3)
f = list(tuples_)
print(f, "\n\n")

"""
A Tuple is a collection of Python objects separated by commas.
In someways a tuple is similar to a list in terms of indexing,
nested objects and repetition but a tuple is immutable unlike lists which are mutable.
"""