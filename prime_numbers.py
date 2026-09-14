def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def print_n_primes(n):
    """Print the first n prime numbers."""
    if n <= 0:
        print("Please enter a positive integer.")
        return

    count = 0
    num = 2
    primes = []

    while count < n:
        if is_prime(num):
            primes.append(num)
            count += 1
        num += 1

    print(f"The first {n} prime numbers are:")
    for i, prime in enumerate(primes, 1):
        print(f"{i}. {prime}")


if __name__ == "__main__":
    n = int(input("Enter the number of prime numbers to print: "))
    print_n_primes(n)

