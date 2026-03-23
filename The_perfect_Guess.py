import random
computer = random.randint(1,101)
you = 0
guesses = 1
while(you != computer):
    you = int(input("Enter a number between 1 and 101 : "))
    if(you>computer):
        print("Lower number please")
    elif(you<computer):
        print("Higher number please")
    guesses += 1
print(f"you have guessed the number correctly in {guesses} attempts.")        


