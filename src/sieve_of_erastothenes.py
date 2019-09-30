def is_prime(num):
    """Determines if a number is prime or not. Returns True if prime and False otherwise

    Arguments:
        num {int} -- number to be checked

    Returns:
        bool -- result of check
    """
    if num > 1:
        for n in range(2, (num // 2) + 1):
            if num % n == 0:
                return False
        else:
            return True
    else:
        return False


# refactor to lambda function
def remove_multiples(ls, num):
    new_ls = []

    for item in ls:
        if item % num != 0 or num == item:
            new_ls.append(item)

    return new_ls


def sieve_of_eratothenes(max):
    prime_numbers = list(range(2, max))

    for num in range(2, max):
        if num * num > max:
            break

        if is_prime(num):
            prime_numbers = remove_multiples(prime_numbers, num)

    return prime_numbers
