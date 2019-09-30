def is_prime(num):
    if num > 1:
        for n in range(2, num // 2):
            if num % n == 0:
                print(f"{num} is not a prime number")
                break
        else:
            print(f"{num} is a prime number")
    else:
        print(f"{num} is a prime number")
