"""Small utilities demo file with fixed functions and safe demo outputs.

Each function is defined without top-level side effects; a demo block
under `if __name__ == '__main__'` prints example outputs.
"""

def welcome(name):
    print(f"Welcome, {name}")


def add(a, b):
    return a + b


def square(n):
    return n * n


def string_reverse(s):
    return s[::-1]


def count_vowels(s):
    count = 0
    for char in s:
        if char in 'AEIOUaeiou':
            count += 1
    return count


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def find_max(numbers):
    return max(numbers)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci_list(n):
    a, b = 0, 1
    res = []
    for _ in range(n):
        res.append(a)
        a, b = b, a + b
    return res


def simple_interest(p, r=5, t=1):
    return (p * r * t) / 100


def string_upper(s):
    return s.upper()


def palindrome(s):
    return s == s[::-1]


def area_of_circle(r):
    pi = 3.141592653589793
    return pi * r * r


def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    # Demo outputs for quick verification
    welcome("Shubhang")
    print("add(5,10) ->", add(5, 10))
    print("square(4) ->", square(4))
    print("string_reverse('hello') ->", string_reverse("hello"))
    print("count_vowels('hello') ->", count_vowels("hello"))
    print("is_prime(7) ->", is_prime(7))
    print("find_max([1,2,3,4,5]) ->", find_max([1, 2, 3, 4, 5]))
    print("factorial(5) ->", factorial(5))
    print("fibonacci_list(7) ->", fibonacci_list(7))
    print("simple_interest(1000) ->", simple_interest(1000))
    print("string_upper('hello') ->", string_upper("hello"))
    print("palindrome('madam') ->", palindrome("madam"))
    print("area_of_circle(5) ->", area_of_circle(5))
    print("gcd(12,15) ->", greatest_common_divisor(12, 15))