def is_prime(num):
    """Determines if a number is prime or not
    Prints a message to stdout

    Arguments:
        num {int} -- number to be determined if prime
    """
    if num > 1:
        for n in range(2, (num // 2) + 1):
            if num % n == 0:
                print(f"{num} is not a prime number!")
                break
        else:
            print(f"{num} is a prime number!")
    else:
        print(f"{num} is not a prime number!")


def accept_input():
    user_input = input("Enter a number: ")

    try:
        int_value = int(user_input)
        return int_value
    except ValueError:
        print("Only integers are allowed: ")
        return 0


print("Determines if a number is prime or not.")
print("Enter 0 to quit!\n")
user_input = accept_input()

while user_input != 0:
    is_prime(user_input)

    user_input = accept_input()

print("Program exited.")
