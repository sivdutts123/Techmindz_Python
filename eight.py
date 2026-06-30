# nested loop
# for i in range(1,6):
#     for j in range(1,6):
#         for k in range(1,6):
#             print(i,j,k)

# for i in range(1,6+1):
#     for j in range(6-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print("*",end="")
#     print()

# for i in range(1,6+1):
#     for j in range(6-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print("*",end="")
#     print()

# for i in range(1,9):
#     for j in range(1,9):
#         if (i + j) % 2 == 0:
#             print("[H]",end = " ")
#         else:
#             print("[T]",end = " ")
#     print()

# rows = 11
# cols = 9
# for i in range(rows):
#     for j in range(cols):
#         if j==0 or j == cols-1 or i==rows//2:
#             print("H",end =" ")
#         else:
#             print(" ",end=" ")
#     print()

# rows = 7
# cols = 5
# for i in range(rows):
#     for j in range(cols):
#         if i==0 or i == rows-1 or j==cols//2:
#             print("H",end =" ")
#         else:
#             print(" ",end=" ")
#     print()

# a = [1,2,3,4,5,6,7,8,9]

# b = []
# c = []
# middle=len(a)//2

# for i in a:
#     if i <= middle:
#         b.append(i)
#     else:
#         c.append(i) 
# print(b)
# print(c)
    