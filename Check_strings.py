"""
Strings - Strings are sequence of charcters with sigle quotes or double quotes
Ex : "hello"
Ex : 'helo'
Ex : "I don't do that"

* String are in orderd sequences it means we can use indexing and slicing to grab the sub sections of the string

Indexing : -
* Indexing notation uses []  notation after the string
* Indexing allows to grab the Single chartcter from the string

Ex Charcter = h e l l o
   Index    = 0 1 2 3 4

* In Python we can use the reverse indexing (if we want to grab the last letter and don't the index we can use revrese indexing)
Ex Charcter = h e l l o
   Index    = 0 -4 -3 -2 -1

Slicing : -
* Slicing allows to grab the sub section of multiple charcter from the string

Syntax
[start:stop:step]
* Start is the numerical index of slice start
* Stop is the numerical indec of slice stop (but not inculded)
* Step is the size of the jump we take from start to Stop

* To Print the string in new line
print("hello \n world")
 o/p : hello world

* To check the length of the String
len(string)

"""
str_1 ="hello"
str_2 = 'nikhil'
str_3 = "this is also a string"
str_4 = "i'm from banaglore"
a= len(str_4)
print(str_1)
print(str_2)
print(str_3)
print(str_4)
print("hello \nworld")
print(len(str_1))
print(type(len(str_2)))
print("length of the String 4 is:", a)
str_5 = str("test")
print(str_5)
#indexing example
my_str="hello world"
print(my_str[0])  #to get the first char of the string
#we can get the element using reverse indexing
print(my_str[-1])
#slicing used to get the sub part of the string
print(my_str[2:]) #will print from 3rd to rest all the charcter
#to get the only the first part
my_str2="ABCDEFGH"
print(my_str2[:4]) #print ABCD
#to get the middle part of the string
print(my_str2[3:6]) #print DEF
print(my_str2[1:4]) #print BCD
#step size if we ommit few charters and get the full string we will use this
my_str3="Bangalore is my city"
print(my_str3[::2]) # it will fetch the 2nd word occurence "Bnaoe"
# we can also add the index is well
print(my_str3[2:10:2]) # start for 2nd char to 10th char and print 2nd occurence element
#to revrese a string
my_str4="nikhil"
print(my_str4[::-1]) #lihkin
