# A simple function get Centigrade return Fahrenheit
def ctof(degree: float) -> float:
    return ((degree * 9) / 5) + 32


# A simple function get Centigrade list return Fahrenheit list

def ctof_list_convertor(c_list: list) -> list:
    return list(map(ctof, test_list_C))


if __name__ == '__main__':

    # list which contain Centigrade
    test_list_C = [-12, 13, 5, 8, 10, 200, 150]

    # list which contain Fahrenheit
    test_list_F = ctof_list_convertor(test_list_C)

    # list which contain centigrade with Analogous Fahrenheit
    CtoF_list = zip(test_list_C, test_list_F)

    # Print CtoF list and force float decimals to 1 point
    for C, F in CtoF_list:
        print(f"{C:3} is {F:5.1f}")
