import sys

numbers = sys.argv
try:
    numbers = list(map(lambda x: float(x), numbers[1:]))
    print(sum(numbers) / len(numbers))
except:
    print("wrong input , only integers and floats")

