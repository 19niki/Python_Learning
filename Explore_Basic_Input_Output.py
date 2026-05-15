"""
- We can get the input from the diffrent files here we are test.txt as example
- We need to save the txt file in the same folder
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"""

#Example 1 - To open and read the data from the file
myfile = open("test.txt")
print(myfile.read()) #print the data which is in test.txt
print(myfile.read()) #will print the null value since the cursour read everything and the end
myfile.seek(0) #Setting cursour back to zero
content =myfile.read() #print the data which is in test.txt
print(content)
myfile.seek(0)
print(myfile.readlines())

#Example 2 - We need to close the file once the usage of the file is done with close() method
print(myfile.close())

#Example 3 - How to close the file we need to use the with operator it will automatically close the file
with open("test.txt") as my_new_file:
    content = my_new_file.read() #here my_new_file is used as the varible for file
    print(content)


#Example 4 - Read Only Parts of the File
with open("test.txt") as my_new_file:
  print(my_new_file.read(5)) #will print this

"""
- If we want open the file from any location of the computer all we need to provide the full path
Syntax - we need to provide the double slash
"D:\\myfiles\\welcome.txt"

"""
myfile1 = open("C:\\Users\\nravindr\\Downloads\\Git Commands.txt")

"""
Reading writing and Appendig Modes
- The open() function takes two parameters; filename, and mode.
- There are four different methods (modes) for opening a file:
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending(will add on to file), creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists
"""
#Example 5 - mode='r'
with open("test.txt", mode="r") as t:
    print(t.read())

#Exaple 6 - mode='a'
with open("test.txt", mode="a") as t:
    t.write("\ntoday is 15.5.2026")

"""with open("test.txt", mode="r") as t:
    print(t.read())"""

#Example 6 - mode='w'
with open("new_test.txt", mode="w") as i:
    i.write("Created the new file")

with open("new_test.txt", mode="r") as j:
     print(j.read())




