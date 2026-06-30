# # def add2(a,b):
# #     return 1, "mohan", True
# # print(add2(1,3))

# # create a calculator using functions.

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b

# def main():
#     while True:
#         print("Welcome to simple calculator !!!!!!!!!!")
#         ch = int(
#             input("Enter your choice : \n1.Add\n2.Sub\n3.Mul\n4.Div\n5.Exit\n:------"))
#         x = int(input("Enter number 1:"))
#         y = int(input("Enter number 2:"))
#         if ch == 1:
#             print(add(x,y))
#         elif ch == 2:
#             print(sub(x,y))
#         elif ch == 3:
#             print(mul(x,y))
#         elif ch == 4:
#             print(div(x,y))
#         elif ch == 5:
#             break
#         else:
#             print("Invalid Value")
    
            
# main()
        
def calculate_age(current_year, current_month, current_day, year_of_birth, month_of_birth, day_of_birth):
    age = current_year - year_of_birth

    if(current_month < month_of_birth) or (current_month == month_of_birth and current_day < day_of_birth):
        age -= 1

    return age


def main():
    print("Welcome to Age Calculator!!!!!!")

    current_year = int(input("Enter the current year:"))
    current_month = int(input("Enter the current month:"))
    current_day = int(input("Enter the current day:"))

    print("\nPlease provide your Date of Birth:")

    year_of_birth = int(input("Enter the year of birth:"))
    month_of_birth = int(input("Enter the month of birth:"))
    day_of_birth = int(input("Enter the day of birth:"))
    
    age = calculate_age(current_year,current_month,current_day,year_of_birth,month_of_birth,day_of_birth)
    print(f"Your are {age} years old")

main()