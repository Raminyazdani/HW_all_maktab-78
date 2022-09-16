from functools import reduce


def power_accum(test: list) -> float or int:
    # lambda x,y:x*y --> it takes two arguments x and y and returns x*y
    # reduce function takes two arguments; first a function and second a list .
    # it will return a single result which will be affected by function part call on the desired list cumulatively
    # Note : reduce function part can take lambda expression too

    return reduce(lambda x, y: x * y, test_list)


if __name__ == '__main__':
    # sample test list
    test_list = [8, 2, 3, -1, 7]

    result = power_accum((test_list))

    # print result
    print(result)
