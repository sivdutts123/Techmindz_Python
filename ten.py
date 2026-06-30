# def add2(a,b):
#     return 1, "mohan", True
# print(add2(1,3))

# create a calculator using functions.

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

def main():
    while True:
        print("Welcome to simple calculator !!!!!!!!!!")
        ch = int(
            input("Enter your choice : \n1.Add\n2.Sub\n3.Mul\n4.Div\n5.Exit\n:------"))
        x = int(input("Enter number 1:"))
        y = int(input("Enter number 2:"))
        if ch == 1:
            print(add(x,y))
        elif ch == 2:
            print(sub(x,y))
        elif ch == 3:
            print(mul(x,y))
        elif ch == 4:
            print(div(x,y))
        elif ch == 5:
            break
        else:
            print("Invalid Value")
    
            
main()
        

        