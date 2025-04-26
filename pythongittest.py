import random
print("Hello, this program will try to guess your age.")
name=input("Enter your name: ")
guess=False
while guess==False:
    guess=random.randint(15,50)
    user_response=input("Are you "+str(guess)+" years old?")
    if user_response.strip()=="y" or user_response.strip()=="Y":
        print("{name} is {guess} years old!")
        quit()
    else:
        print("Im sorry")
