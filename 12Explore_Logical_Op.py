"""
Logical Operators

No  Operator	 Description	                                Example
1. and 	       Returns True if both statements are true	        x < 5 and  x < 10
2. or	       Returns True if one of the statements is true	x < 5 or x < 4
3. not	       Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

Identity operators
is 	 - Returns True if both variables are the same object	x is y
is not - 	Returns True if both variables are not the same object	x is not y

"""
a =10
b= 5
c = 34
print(a > b and a >c)
print (b>c and c>a)
print(("h" == "h") and (2==2))
print(a>b or b>c)
print(not a>b or b>c)
print(not (a>b or b>c))

print("Identity operators")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) #true
print(x is y) #false
print(x == y) #true
"""
Difference Between is and ==
is - Checks if both variables point to the same object in memory
== - Checks if the values of both variables are equal
"""

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y) #true
print(x is y) #false

"""
Membership Operators
Membership operators are used to test if a sequence is presented in an object:
in 	 - Returns True if a sequence with the specified value is present in the object	 ex:x in y	
not in - Returns True if a sequence with the specified value is not present in the object ex:x not in y
"""

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)#true

num= [1,2,3,5]
print(2  in num and 7 not in num) #true

names = {"niki","akhil","ravi"}
print("niki" in names)

a=34
b=12
c=90
if a>b and a>c:
    print("a is big")
else:
    print("b is big")

