class Book:
    count = 0

    def __init__(self, title, price, count_book):
        self.title = title
        self.price = int_maker(price, "price")
        count_book = int_maker(count_book, "book count")
        self.count_book = int_maker(count_book, "book count",(count_book>0))

        Book.count += 1

    def __str__(self):
        return f"book name : {self.title}, price : {self.price}, count : {self.count_book}"


def int_maker(test, input_type, criteria=None):
    while True:
        try:
            test = int(test)
            if criteria == None:
                return test
            else:
                if criteria:
                    return test
                else:
                    raise
        except:
            test = input(f"wrong input for {input_type} please enter a valid one:\n-->\t")
            try:
                return int_maker(test, input_type, (int(test) > 0))
            except:
                continue


def check_count(test):
    while True:
        if test >= 0:
            return True
        else:
            return False


if __name__ == '__main__':

    Book()