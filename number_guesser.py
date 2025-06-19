import random

user = int(input("Enter a number between 1 to 20: "))
print(f"You entered number {user}")

r = random.randrange(1,21)
print(f"random number is {r}")


if r == user:
    print("You guessed the right number")
else:
    print("Incorrect answer")