def sorting_e2(test: list) -> list:
    return sorted(test, key=lambda x: x[1])


if __name__ == '__main__':
    # defining test list
    test = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    # result using sorted function
    result = sorting_e2(test)
    print(result)
