#list

#collection of data []

# a=[1,2,3,4,5,6]
# properties
# list can have any element of any size

# data = [1,2.2,"mohan",True]

# list are ordered
# a = [1,2,3,4]
# b = [3,2,1,4]

# print(a == b)

# lists are indexed 

# a =[11,12,13,14,15,16,17,19,20]

# print(a)
# print(a[0])
# print(a[4])
# print(a[0:5])
# print(a[0:5:2])
# print(a[::-1])

# list are mutable
# changable
# str immutable

# a= [11,12,13,14,15,16,17]
# (a[0:2])=[31,32,33,34,35]
# print(a)

# a= [11,12,13,14,15,16,17,18,34]
# a[0:5] = ['mohan']
# print(a)

# lists are nested

# a = [11,12,[100,300,200],14,15]
# print(a[2][2])

# inbuilt methods
# to add elements
# append(): adds an element to the end of the list
# a= [11,12,13,14,15]
# a.append(100)
# a.append(200)
# print(a)

# extend(): adds an iterable to the list
# a = [11,12,13,14,15]
# a.extend([23,24,'mohan'])
# print(a)

# insert() : (index,value)

# a = [11,12,13,14]
# a.insert(1,"mohan")
# print(a)

# to remove elements
#remove
#pop

# a = [11,12,13,14,15]
# a.remove(11)
# print(a)

# a = [11,12,13,14,15,12,234,45,6,11]
# a.pop(0)
# a.pop(2)
# a.pop(7)
# print(a)

# tuple
# collection of data
# a = (2,3,1,"mohan",672,32,2,23)
# ordered
# indexed
# immutable

# a =(1,2,3,4)
# print(a[::-1])

# str,list,tuple,set,dict - itreables

fruits = ["apple","orange","grapes","banana"]
for i in range(3, len(fruits)):
    print(i,fruits[i])