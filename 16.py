# # inheritance
# # parent class
# # child class

# class p1:
#     def __init__(self):
#         pass
#     def walk(self):
#         print("person can walk ")
#     def smile(self):
#         print("person can smile hahahahah")

# class p2(p1):
#     def __init__(self):
#         pass
#     def read(self):
#         print("person can read ")
#     def smile(self):
#         print("person can write")

# person2 = p2()
# person2.smile()
# person2.walk()





# class p1:
#     def __init__(self):
#         pass
#     def walk(self):
#         print("person can walk ")
#     def smile(self):
#         print("person can smile hahahahah")

# class p2(p1):
#     def __init__(self):
#         pass
#     def read(self):
#         print("person can read ")
#     def smile(self):
#         print("person can write")

# person2 = p2()
# person2.smile()
# person2.walk()


# polymorphism

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self,otr):
        return self.m1+self.m2,otr.m1+otr.m2
    
s1 = Student(7,8)
s2 = Student(6,10)


print(s1+s2)

