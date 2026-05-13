"""
- Sets are unorderd elemets of the unique elements so they don't allow duplicates.
Syntax - varible = {"value1", "value2", "value3"}

"""

#We can add the values to via two ways
#Example 1
myset1 = set()
myset1.add("nikhil")
print(myset1)

#Example 2 - Add the values directly
myset2 = {'nikhil','ravi','akhil'}
print(myset2)

#set will not allow dupliacts
"""
Unordered and Unchnagble
- Unordered means that the items in a set do not have a defined order.
- Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
- Set items are unchangeable, meaning that we cannot change the items after the set has been created.
"""
myset3 = {4,1,1,2,2,2,2,3}
print(myset3) #{1, 2, 3}

print(set("nikhil")) #will print the char {'i', 'n', 'l', 'k', 'h'}

#Example 3  - add new elements to set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange") #{'orange', 'cherry', 'banana', 'apple'}
print(thisset)

#Example 4 - Add one set to another using update() method
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#Example 5 -
# Add any iterable The object in the update() method does not have to be a set,
# it can be any iterable object (tuples, lists, dictionaries etc.)
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#Example 6 - Remove item from the set using remove() method
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)



