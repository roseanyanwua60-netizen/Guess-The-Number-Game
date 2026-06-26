import random
secret_number = random.randint(1, 10)
print("welcome to guess the number!")
print("i am thinking of a number between 1 and 10.")
guess = int(input("enter your guess: "))
if guess == secret_number:
    print("CONGRATULATIONS! you guessed correctly!")
else:
        print("wrong guess!")
        print("the correct number was", secret_number)
        print("Try again")
