#Write an equation that uses multiplication,
# division, an exponent, addition, and subtraction that is equal to 100.25.

print(4 * (6 + 5)) #44
print(4 * 6 + 5 ) #29
print(4 + 6 * 5 ) #34

#What is the type of the result of the expression 3 + 1.5 + 4?
print(type( 3 + 1.5 + 4))

#What would you use to find a number’s square root, as well as its square?
print(6**2) #to find square
print(36 ** 0.5)

s = 'hello'
print(s[1])
print(s [::-1])
print(s[4:])
print(s[-1])

#Build this list [0,0,0] two separate ways.
list1= [0,0,0]
list2 = [0]*3
print(list2)
list3 = [1,2,[3,4,'hello']]
print(list3[2][2])
list3[2][2]="goodbye"
print(list3[2][2])
list4 = [5,3,4,6,1]
list4.sort()
soretd_num_list=list4
print(soretd_num_list)


d = {'simple_key':'hello'}
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d["k1"][0]["nest_key"][1])

# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2])

list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
print(l_one[2][0] >= l_two[2]['k1']) #3

