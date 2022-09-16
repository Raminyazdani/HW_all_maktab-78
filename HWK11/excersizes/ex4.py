import argparse
import random


def guess_game(start, end, test, score):
    guess = test
    while True:
        if start < guess < end:
            if guess == score:
                print("you won")
                return 0
            elif guess > score:
                print("your number is higher than the goal")
                return 1
            else:
                print("your number is lower than the goal")
                return 2
        else:
            print(f"number most between {start} and {end}")
            guess = int(input("number : "))


parser = argparse.ArgumentParser(description="python script for calculating averages")
try:
    parser.add_argument("guessing_game", type=int)
except:
    pass
parser.add_argument("-g", "--guess", type=int, required=False)
parser.add_argument("-s", "--start", type=int, required=False, default=0)
parser.add_argument("-e", "--end", type=int, required=False, default=100)

lives = 5
args = vars(parser.parse_args())



if args["guessing_game"] and args["guess"]:
    raise ValueError("You must specify only guess with or without -g")
elif args["guessing_game"]:
    args["guess"] = args["guessing_game"]


while args["start"] > args["end"]:
    print("starting number > ending . its wrong :D")
    while True:
        try:
            args["start"] = int(input("start : "))
            break
        except:
            print("Invalid format for number")
            continue
    while True:
        try:
            args["end"] = int(input("end : "))
            break
        except:
            print("Invalid format for number")
            continue

score = random.randint(args["start"], args["end"])
print(score)

if not args["guess"]:
    while True:
        try:
            print("lives == 5")
            x = int(input("your guess : "))
            args["guess"] = int(x)
            cond = guess_game(args["start"], args["end"], args["guess"], score)
            lives -= 1
            break
        except:
            print("wrong guess value only integer")
else:
    print("lives : ", lives)
    cond = guess_game(args["start"], args["end"], args["guess"], score)
    lives -= 1

while lives >= 1 and cond != 0:
    print("lives : ", lives)
    while True:
        try:
            args["guess"] = int(input("your number : "))
            break
        except:
            print("wrong guess value only integer")
    cond = guess_game(args["start"], args["end"], args["guess"], score)

    if cond == 0:
        break
    lives -= 1

if cond != 0:
    print("you lose")
