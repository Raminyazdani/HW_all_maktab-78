# input user
if __name__ == '__main__':

    test = input().replace(" ","").swapcase()
    vowels = ["a","i","o","u","e"]
    for char in vowels:
        test = test.replace(char, ".")
        test = test.replace(char.upper(), ".")
    print(test)