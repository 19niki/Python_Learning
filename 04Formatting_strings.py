"""
If we want to inject the String to the with the varible often we use format() or fstrings() - Formatted string litterals
Ex : age = 36
#This will produce an error:
txt = "My name is John, I am " + age
print(txt)

In order to overcome this we c=use python methods.
"""

"""
1. Format() - The format() method formats the specified value(s) and insert them inside the string's placeholder.
The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.

Syntax - string.format(value1, value2...)
Ex:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
"""

#Example 1
text1 = "My name is {}".format("Nikhil")
print(text1) #My name is Nikhil

text2 = "My nam is {}, and i am {} years old"
print(text2.format("Nikhil",30)) #My nam is Nikhil, and i am 30 years old

#we can also pass the value based on the index
text3 = "in {0} the heat is {1} degree"
print(text3.format("Bangalore",40))

#we can also assign the values based on the keyword aka varible assignment
text4 = "i am {age} years old and i live {city} from past {years}"
print(text4.format(age=30,city="Bangalore",years=40))

#float formatting values
#syntax - {value:width.persion f} -- Width will add the white spaces
num = 100/777
print(num)
print("the {n:1.3f} is the result".format(n=num))

"""
Formated string literals
"""
#example 2
age =23;
print(f"Nikhil age is {age}")

#example 3
name ="Nikhil"
age = 29
str1 = f"{name} is {age} years old."
print(str1)

#example 4
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)