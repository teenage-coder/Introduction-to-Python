import random

guess = int(input("Enter a number between 0 - 9: "))

num = random.randint(0,9)

if ( guess == num ): 
    print("Congrats, You've guessed a correct number!")

else:
    print("Sorry, You lose!")

print(num)
