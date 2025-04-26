import random
print("Hello, this program will try to guess your age.")
name=input("Enter your name: ")
guess=False
while guess==False:
    guess=random.randint(15,30)
    user_response=input("Are you "+str(guess)+" years old?")
    if user_response=="y" or user_response=="Y":
        print("{name} is {guess} years old!")
        quit()
    else:
        print("Im sorry")
