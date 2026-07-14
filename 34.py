# sum of digits in a number 

# input - 15432
# output - 15

# num = int(input("Enter a number:"))

# digit_sum = 0
# original_sum = num

# while num > 0:
#     last_digit = num % 10
#     num = num//10
#     digit_sum = digit_sum + last_digit

# print(f"The Sum of the {original_sum} is: {digit_sum}")

# reverse of a number
# 456
# 654
# num = int(input("Enter the number:"))

# original_num = num
# reversed_num = 0

# while num > 0:
#     last_digit = num % 10
#     reversed_num = (reversed_num * 10) + last_digit
#     num = num//10

# print(f"The reverse of {original_num} is : {reversed_num}")

# num = int(input("Enter the number :"))
# factorial = 1
# original_num = num

# while num > 0:
#     factorial = factorial * num
#     num = num - 1

# print(f"The factorial of {original_num} is : {factorial}")

# for loop

# # for i in range(start, stop, step):
# for i in range(1,23,4):
#     print(i)

# total_sum = 0
# for i in range(1,101):
#     total_sum = total_sum + i
# print(f"The sum of 100 numbers is : {total_sum}  ")


# num = int(input("Enter the number:"))
# factorial = 1
# original_num = num
# for num in range(1,num,6):
#     factorial = factorial * num
# print(f"The factorial of {original_num} is: {factorial}")

# num = int(input("Enter the number:"))
# print(f"\nThe Multiplication Table of {num}:")

# for i in range(1,11):
#     result = num * i

#     print(f'{num} X {i} = {result}')


# count = int(input("Enter num count:"))
# sum = 0
# for i in range(count):
#     num = int(input("Enter your num:"))
#     sum = sum + num
# print(f"sum is {sum}")
# print(f"Average = {sum/count}")


# a, b = 0, 1
# for i in range(10):
#     print(a, end=" ")
#     a, b = b, a + b




# num = int(input("Enter the number:"))
# a = 0
# b = num13
# while num > 0:
#     c = num % 10
#     num = num//10
#     a = a + c
# print(f"The sum of all {b} is:{a}")



# class - blueprint(to create objects)

# class car:
#     def __init__(self,n,c):
#         self.name = n
#         self.color = c
#         print("object created")
#     def start(self):
#         print(f"{self.name} has started")
#     def stop(self):
#         print("car stopped")
# c1 = car("swift","black")
# c2 = car("city","red")
# c2.start()
# c1.stop()

# constructor - used to initialize an object (__init__())
# initialize


# create a class student
# with 6 attributes name, m1, m2, m3, m4, m5

# 3 methods

# sum_of_marks()
# average_of_marks()
# display()

# class student:
#     def __init__(self,name,m1,m2,m3,m4,m5):
#         self.name = name
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#         self.m4 = m4
#         self.m5 = m5

#     def sum_of_marks(self):
#         return self.m1+self.m2+self.m3+self.m4+self.m5
#     def average_of_marks(self):
#         return self.sum_of_marks()/5
#     def display(self):
#         print(f"student {self.name} has marks of {self.m1},{self.m2},{self.m3},{self.m4},{self.m5} with {self.m1+self.m2+self.m3+self.m4+self.m5} as sum and average marks as {(self.m1+self.m2+self.m3+self.m4+self.m5)/5}")


# s1 = student("joel",45,56,67,53,43)
# s1.display()
# s1.average_of_marks()
# s1.sum_of_marks()