# loops,break,continue,pass
# num = int(input("Enter the number:----"))
# prime = True
# if num <= 1:
#     prime = False
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             prime = False
#             break
# if prime:
#     print("This is a prime number ")
# else:
#     print("This is not a prime number ")
          
# # input n words and make it into a sentence 
# sentence = ""
# print("Let's build a sentence!")
# print("Type 'STOP' when you are finished.")
# print("-" * 30)
# while True:
#     word = input("Enter a word: ")

#     if word == "STOP":
#         break
#     if word == "":
#         print("You didn't type anything! Try again.")
#         continue

#     sentence = sentence + word + " "

# print("-" * 30)
# print("Your complete sentence is:",sentence)
 
#set : collection of data
# a = {1,2,3}
# b = {2,1,3} unordered, unindexed, containing no duplicate values.
# print(a == b)

# fruits = {1,2,3,"Pankaj","Ajel","Sivdutt",34,23,45}

# for i in fruits:
#     print(i)
# a ={1,2,3,4,5,6}
# b ={7,8,9,1,2,3}
# print(a|b) - union

# a ={1,2,3,4,5,6}
# b ={7,8,9,1,2,3}
# print(a&b) - Intersection
# print(a-b)
# print(b-a)

# DICTIONARY
# key value paired datatype
# key : "Value"
# userdata =  {"name":"mohan","age":27,"location":"kochi"}
# #index X
# print(userdata["age"])
# print(userdata["location"])
# #mutable

# data = {}
# print(type(data))

# data = {}
# data["name"] = "ajel Anaya"
# data["Age"] = 22
# data["email"] = "ajelvarghesemathew@gmail.com"
# print(data)


#restrictions
#1.keys are unique
#2.keys are immutable 
#get()
#keys()
#values()
#update()
#pop()
#popitem()
#clear()
a = {"name":"mohan","age":30,"location":"kochi"}
print(a.get("name"))
print(a['location'])
print(a.keys())
print(a.values())
print(a.items())
a.update({'phone':34456789})
a['age']= 50
a.pop("name")
a.popitem()
a.clear()
print(a)

