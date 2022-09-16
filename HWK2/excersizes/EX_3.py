# function for primality check
def isprime(number: int) -> bool:
    # To check number primality , must check from 2 to √n
    start = 2
    end = int(number ** 0.5) + 1

    # return False if not prime and True if prime
    for checker in range(start, end):
        if number % checker == 0: return False
    return True


if __name__ == '__main__':
    # test check for 12
    print(isprime(12))

    # test check for 7
    print(isprime(7))
