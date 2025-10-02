import math
import random


def sphere_volume(r):
    return (4/3) * math.pi * (r**3)


def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]


def filter_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    return [x for x in numbers if is_prime(x)]


def guess_number(name):
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    guesses = 0
    guess = 0
    while guess != number:
        print("Take a guess.")
        guess = int(input())
        guesses += 1
        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
    print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
