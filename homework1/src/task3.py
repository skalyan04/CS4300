# task3.py

def check_number(num):
    """Check if a number is positive, negative, or zero."""
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


def get_first_primes(n=10):
    """Return the first n prime numbers using a simple algorithm."""
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


def is_prime(num):
    """Helper function to check primality."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def sum_1_to_100():
    """Return the sum of numbers from 1 to 100 using a while loop."""
    total = 0
    i = 1
    while i <= 100:
        total += i
        i += 1
    return total


if __name__ == "__main__":
    print("Check number -5:", check_number(-5))
    print("Check number 0:", check_number(0))
    print("Check number 7:", check_number(7))

    print("First 10 primes:", get_first_primes(10))

    print("Sum 1 to 100:", sum_1_to_100())
