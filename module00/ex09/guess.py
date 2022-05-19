import sys
import random

n = random.randint(1, 99)

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")
print("What's your guess between 1 and 99?")
print(">> ", end="")
number = -1
input = ""
cmp = 0
while True:
    sys.stdout.flush()
    try:
        input = sys.stdin.readline()
        number = int(input)
    except ValueError:
        if (input.strip() == "exit"):
            print('Goodbye!')
            exit()
        print("what you enter is not a number")

    if (number > 0 and number < 100):
        cmp += 1
        if number < n:
            print('Too low!')
        elif number > n:
            print('Too high!')
        elif number == n:
            if number == 42:
                print('The answer to the ultimate question of life, the universe and everything is 42.')
            if cmp == 1:
                print('Congratulations! You got it on your first try!')
            else :
                print("Congratulations, you've got it!")
                print("You won in {} attempts!".format(cmp))
            exit()
    else:
        print('your guess should be between 1 and 99')
    print("What's your guess between 1 and 99?")
    print(">> ", end="")