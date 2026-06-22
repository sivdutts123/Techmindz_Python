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
          
# input n words and make it into a sentence 
sentence = ""
print("Let's build a sentence!")
print("Type 'STOP' when you are finished.")
print("-" * 30)
while True:
    word = input("Enter a word: ")

    if word == "STOP":
        break
    if word == "":
        print("You didn't type anything! Try again.")
        continue

    sentence = sentence + word + " "

print("-" * 30)
print("Your complete sentence is:",sentence)
 








