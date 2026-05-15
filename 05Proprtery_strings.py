"""
String are immutable in Python onece the value assigned it cannot be changed

"""
from dataclasses import replace

from Check_strings import my_str

"""String Concation -  Adding of  two string is called String concation"""
#Example 1
str1 = "Hello"
str2 = "World"
print(str1 + str2) #HelloWorld
print(str1 +" "+str2) #Hello World

#Example 2
x= "I am from banaglore"
print(x +" "+"and i work in bangalore")
# To replace i to you from varibel x
y=x[4:]
print("Are you"+y)

#Example 3
#we can also print particular letter 10 times with * symbol
letter = 'a'
print(letter * 10) #will print letter 10 times

#Example 4
#upper case and lower case
#The upper() method returns the string in upper case:
#The lower() method returns the string in lower case:
my_str="Hello World"
print(my_str.upper())
print(my_str.lower())

#Remove Whitespace - The strip() method removes any whitespace from the beginning or the end:
str3 = " this is india "
print(str3.strip())

#Replace String  - The replace() method replaces a string with another string:
str4  = " paychex is my compnay"
print(str4.replace("paychex", "izmo"))

#Split String - The split() method splits the string into substrings if it finds instances of the separator:
# if the seprator is not mentioned it will seprate from white spaces.
print(str4.split()) #['paychex', 'is', 'my', 'compnay']