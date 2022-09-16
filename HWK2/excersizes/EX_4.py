# function for zipping using ordered_dict
def algorythm_zip(number: str) -> str:
    test = number
    # dict can store keys numbers and repeats
    numbers_dict = dict()
    for digit in test:
        numbers_dict[digit] = numbers_dict.get(digit, 0) + 1

    numbers = list(numbers_dict.keys())
    repeats = list(map(lambda x: str(x), filter(lambda x: x > 1, numbers_dict.values())))
    # making result
    result = []
    result.extend(repeats)
    result.extend(numbers)
    result.sort()
    result = "".join(result)

    # reccursive test for final result
    if test == result:
        return result
    else:
        return algorythm_zip(result)


if __name__ == '__main__':
    item = "64422545456"
    print(algorythm_zip(item))
