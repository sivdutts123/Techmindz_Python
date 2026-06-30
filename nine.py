# hollow square
# for i in range(1,8):
#     for j in range(1,8):
#         if i == 1 or i == 7 or j == 7 or j == 1:
#             print("#",end = "")
#         else:
#             print(" ",end ="")
#     print()

# to print s
for i in range(1,8):
    for j in range(1,6):
        if i == 1 or i == 4 or i == 7 or (j == 1 and ( i == 2 or i == 3))or (j == 5 and (i == 5 or i == 6)):
            print("#",end = "")
        else:
            print(" ",end = "")
    print()