import random

number = random.randint(1, 10)
attempt = 0

while attempt<= 3:
 user_guess = int(input("guess the number between 1 to 10"))
 if(user_guess>10 or user_guess<0):
    print("please enter the valid")

 else:
    if (number==user_guess):
      print("badhai cha you won!!!!")
      break
    elif (user_guess<number):
      print("your guess is low,please guess higher number ")
     

    else:
     print("your guess is high,please guess a lower number")         
