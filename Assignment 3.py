# apple triangle pattern
word = "APPLE"
for i in range(1,len(word)+1):
    for j in range(len(word)+1,i,-1):
        print(" ",end="")
    for k in range(0,i):
        print(word[k],end=" ")
    print()