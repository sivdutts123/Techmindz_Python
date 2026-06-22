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

# fruits = ["apple","orange","grapes","banana"]
# for i in range(3, len(fruits)):
#     print(i,fruits[i])

# # fibanocci series
# # amstrong number
# # prime number

# find vowels and their positions in a string
# a = hari
# a at location 1
# i at location 3

# a = "hari"

# for i in range(len(a)):
#     if a[i] == 'a' or a[i] == 'e' or a[i] == 'i' or a[i] == 'o' or a[i] == 'u':
#         print(f"{a[i]} at index {i}")


# a = input("Enter the name:")
# for i in range(len(a)):
#     if a[i] == 'a' or a[i] == 'e' or a[i] == 'i' or a[i] == 'o' or a[i] == 'u':
#         print(f"The Vowels and positions in given string is {a[i]} at index {i}")
   
# a = int(input("Enter the number:"))
# even = []
# odd = []
# for i in range(0,a+1):
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
#         print(f"The list of even numbers from {a} is {even}")
#         print(f"The list of odd numbers from {a} is {odd}")


# # c =[1,2,3,4,1,3,4,2,7,8,9,2,3,4,5]
# # remove duplicates from this list

c =[1,2,3,4,1,3,4,2,7,8,9,2,3,4,5]
b = []
for i in c:
    if i not in b:
        b.append(i)
print(f"The duplicate removed list is {b}")


