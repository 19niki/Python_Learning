"""
- Dicitionaries are unordered mapping for storing objects
- Dictionaries are used to store data values in key:value pairs.
- This kep value pair allow to access the elements without knowing index location

Syntax : {'key1':'value1','key2':'value2'}
Diff b/w Dicitionaries and list
Dicitionaries - Objects retrived by key name, Unordered and cannot be sorted

Lists - Objects retrived by key location, Ordred sequence can be indexed or sliced

"""
#Example 1
my_dict = {'key1':'value1','key2':'value2'}
print(my_dict) #{'key1': 'value1', 'key2': 'value2'}

#to print the value using the key
print(my_dict['key1'])  #value1

#Example 2
my_info = {'name':'Nikhil',
           'age':29,
            'city':'Shimoga'}
print(my_info['age'])

#Example 3 - We can also store the list or another dictionaries in the dictionaries
my_dict1 = {"one":1,"two":[0,1,2],"three":{"insidekey":10}}
print(my_dict1["two"]) #[0, 1, 2]

# to get the inside key
print(my_dict1["three"]["insidekey"]) #10

#to get the particular item for list inside dict
print(my_dict1["two"][2]) #2

#Example 4 - To get all spefic elemets from list and do manuplation
my_dict2 = {"alpha":['a','b','c'],"num":1}
print(my_dict2["alpha"][1].upper()) # Will print B in upper

#Example 5  - To add the new key value to the dict
my_dict3 = {"k1":1,"k2":2,"k3":3}
my_dict3["k4"] =4
print(my_dict3)

#to get the length we use len() method
print(len(my_dict3))

#Example 5 - we can alos get only key and vaulue and all the item using keys(),values(),items()
print(my_dict3.keys()) #dict_keys(['k1', 'k2', 'k3', 'k4'])
print(my_dict3.values()) #dict_values([1, 2, 3, 4])
print(my_dict3.items()) #dict_items([('k1', 1), ('k2', 2), ('k3', 3), ('k4', 4)])

#Duplicates Not Allowed
#Dictionaries cannot have two items with the same key: Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#Example 6 - Update Dictionary
#The update() method will update the dictionary with the items from the given argument.
#The argument must be a dictionary, or an iterable object with key:value pairs.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

#Example 7 - Remove item
#We can use the pop() to remove the item for the dist
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
    "year": 1964
}
thisdict.pop("brand")
print(thisdict)