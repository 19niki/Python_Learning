"""
 - List are ordred sequcence that can hold a variety of object types
 - They use square bracket and commas to seprate the objects in the list
 - [1,2,3,4]
 - List support indexing and slicing and can be nested and also have  a variety of unsfull methods
 - Lists are one of 4 built-in data types in Python used to store collections of data,
   the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

 - List items are ordered, changeable, and allow duplicate values.
 - List items are indexed, the first item has index [0], the second item has index [1] etc.

"""
# Example 1
my_list1 = [10,20,30]
#it can also contaion diffrent data types
my_list2 = ["Nikhil", 233, 43.12]
print(my_list1)
print(my_list2)

#Example 2
#len() function is used to get the length of the function
print(len(my_list1))

#Example 3
#we can also to slicing and indexing on the strings
print(my_list1[0]) #10
print(my_list1[:2]) #10,20
print(my_list2[2:]) #43.12

#Example 4
# We can also concate two string uisng arthmetic operator
first_list = [10,20,65]
second_list = [88,87,23]
final_list = first_list + second_list
print(final_list)

#Example 4
#list are muttable we can change the value using the index
my_list3=["Cat", "Dog", "Fish","Lion"]
my_list3[0]="fox"
print(my_list3[0:3]) #fox, dog, fish

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) # will replace  "banana", "cherry" with "blackcurrant", "watermelon"

#Example 5
#We can add the items to the list using append() method
my_list4 = ['one','two','three','four','five']
my_list4.append('six')
print(my_list4)

"""
To Insert the method
we can also use insert() method to insert the item to the list
"""
#Example 6
my_list4 = ['one','two','three','four','five']
my_list4.insert(0,'zero')
print("Example 6:", my_list4)

#Example 7
#We can append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) # append the 2nd list item to the 1st list
print(thislist)


#Example 8
#We can remove the specific element from the list using remove() method
my_list5=["one","two","three","four","five","six","seven","eight","nine"]
my_list5.remove("one")
print(my_list5) #removes one

#We can remove the specific element from the list using index by pop() method
my_list5.pop() # it will remove the final element by default pop(-1)
print(my_list5)

#we can also remove the spefic element with index
my_list5.pop(2)
print(my_list5) # it will remove four

#Example 9
#We can sort the list using the sort() method
num_list=[65,22,6,43,21,13]
alpha_list=['r','b','t','y','e']
num_list.sort()
soretd_num_list=num_list #how to assign the value
print(soretd_num_list) #[6, 13, 21, 22, 43, 65]
alpha_list.sort()
print(alpha_list)

"""
Sort Descending
To sort descending, use the keyword argument reverse = True:

"""
num_list.sort(reverse=True) #[65, 43, 22, 21, 13, 6]
print(num_list)

#Example 10
# we can also reverse the string using the reverse() method
num_list2=[10,43,22,21,90]
num_list2.reverse()
print(num_list2) #[90, 21, 22, 43, 10]


#Example 11
#We can also empty or clear the whole list
num_list2.clear()
print(num_list2) #[]


