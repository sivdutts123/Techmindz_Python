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




num = int(input("Enter the number:"))
a = 0
b = num
while num > 0:
    c = num % 10
    num = num//10
    a = a + c
print(f"The sum of all {b} is:{a}")






