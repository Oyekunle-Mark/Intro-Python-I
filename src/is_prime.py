def is_prime(num):
    """Determines if a number is prime or not
    Prints a message to stdout

    Arguments:
        num {int} -- number to be determined if prime
    """
    if num > 1:
        for n in range(2, (num // 2) + 1):
            if num % n == 0:
                print(f"{num} is not a prime number")
                break
        else:
            print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")


user_input = input("Enter a number: ")
is_prime(int(user_input))
