# control statements

#loops

#while
#condition based Loop 

# while True:
#     print("Mohan")

# i = 1
# while True:
#     print(i)
#     i = i + 1

# i = 1
# sum = 0
# while i <= 10:
#     sum = sum + i
#     i = i + 1
# print(sum)

i = 1
sum_even = 0
odd_sum = 0

while i <= 100:
    if i%2 == 0:
        sum_even = sum_even + i
    else:
        odd_sum = odd_sum + i

    i = i + 1

print("Print sum of even numbers", sum_even)
print("Print sum of odd numbers",odd_sum)