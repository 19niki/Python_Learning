"""
- Tuples are very similar to lists which are used to store multiple items in a single variable.
- A tuple is a collection which is ordered and unchangeable.
- Tuples are immutable, Once the value assigned cannot be reassigned.
- Tuples allow duplicate values.
synatx : varible = ("value1","value2","value3")
ex: mytuple = ("apple", "banana", "cherry")

"""

#Example1
my_tup1=("apple", "banana", "cherry")
my_list1=["apple", "banana", "cherry"]
print(my_tup1)
print(my_list1)
print(type(my_tup1))
print(type(my_list1))

# to find the length using the len()
my_tup2=("nikhil",29,"udupi")
print(len(my_tup2))

#Example2 - We can also do the slicing and indexing to get the spefic value
colors=("red","green","blue")
print(colors[0])
print(colors[:2])
print(colors[2:])

#Example3 - We have count() method to count the occurence of the spefic value
colors1=("red","green","blue","red")
print(colors1.count("red")) #2

"""
Change tuples values
- Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
- But there is a workaround. You can convert the tuple into a list, change the list, 
 and convert the list back into a tuple.
"""
#Example 4
my_tup3=(1,2,3,4)
#my_tup3[2] = 5 will throw error if we do reassign
print("Before change")
print(my_tup3) #(1, 2, 3, 4)

#converting tuple to list and doing modification

list2=list(my_tup3)
list2[2]=5
my_tup3=tuple(list2)
print("After change")
print(my_tup3) #(1, 2, 5, 4)

#Example 5 - adding another tuple to another
my_tup4 = ("apple", "banana", "cherry")
test = ("mango",)
my_tup4 = my_tup4 + test
print(my_tup4)