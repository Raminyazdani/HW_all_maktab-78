# must import Ordereddict because output is sort by the entry order of string
from collections import OrderedDict


def char_count(test: str) -> dict:
    result = OrderedDict()
    for char in test:
        result[char] = result.get(char, 0) + 1
    return dict(result)


if __name__ == '__main__':
    item = "www.google.com"
    print(char_count(item))
