def ounces(grams):
    return grams * 28.3495231


g = float(input("grams: "))
oz = ounces(g)
print(f"{g} grams = {oz} ounces")

#task2

def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)


f = float(input("Enter temperature in Fahrenheit: "))
c = fahrenheit_to_celsius(f)
print(f"{f}°F = {c}°C")
 
 #task3
def solve(numheads, numlegs):
    r = (numlegs - 2 * numheads) // 2
    c = numheads - r
    return c, r


heads = 35
legs = 94

chickens, rabbits = solve(heads, legs)
print(f"Chickens: {chickens}, Rabbits: {rabbits}")

#task4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [x for x in numbers if is_prime(x)]


nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Prime numbers:", filter_prime(nums))

#task5

def permute(s, prefix=""):
    if len(s) == 0:
        print(prefix)
    else:
        for i in range(len(s)):
            new_s = s[:i] + s[i+1:]
            permute(new_s, prefix + s[i])


text = input("Enter a string: ")
permute(text)

#task6
def reverse_words(s):
    words = s.split()
    words.reverse()
    return " ".join(words)

text = input("Enter a sentence: ")
print(reverse_words(text))

#task7

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


user_input = input("Enter numbers separated by space: ")
nums = [int(x) for x in user_input.split()]

print("Result:", has_33(nums))

#task8

def spy_game(nums):
    code = [0, 0, 7]
    for n in nums:
        if n == code[0]:
            code.pop(0)
        if len(code) == 0:
            return True
    return False


nums = list(map(int, input("Введите числа через пробел: ").split()))
print("Результат:", spy_game(nums))

#task9
import math

def sphere_volume(r):
    return (4/3) * math.pi * (r**3)


r = float(input("r: "))
print( sphere_volume(r))

#task10
def unique_list(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst


nums = list(map(int, input("list: ").split()))
print(unique_list(nums))

#task11
def is_palindrome(word):
    word = word.lower()
    n = len(word)
    for i in range(n // 2):  
        if word[i] != word[n - 1 - i]:  
            return False
    return True

text = input("Введите слово или фразу: ")

if is_palindrome(text.replace(" ", "")):
    print("polindrome")
else:
    print("not polindrome")

#task12
def histogram(lst):
    for num in lst:
        print("*" * num)


nums = list(map(int, input("numbers: ").split()))
histogram(nums)

#task13
import random

print("Hello! What is your name?")
name = input()

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

#task14

movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

def is_above_55(movie):
    return movie["imdb"] > 5.5

def high_rated_movies(movies):
    return [m for m in movies if m["imdb"] > 5.5]

def movies_by_category(movies, category):
    return [m for m in movies if m["category"].lower() == category.lower()]

def average_imdb(movies):
    total = sum(m["imdb"] for m in movies)
    return total / len(movies)

def average_imdb_by_category(movies, category):
    cat_movies = movies_by_category(movies, category)
    if not cat_movies:
        return 0
    total = sum(m["imdb"] for m in cat_movies)
    return total / len(cat_movies)

print("1. Проверка одного фильма (Usual Suspects):", is_above_55(movies[0]))
print("\n2. Фильмы с рейтингом > 5.5:")
for m in high_rated_movies(movies):
    print("-", m["name"], m["imdb"])

print("\n3. Фильмы категории Romance:")
for m in movies_by_category(movies, "Romance"):
    print("-", m["name"], m["imdb"])

print("\n4. Средний рейтинг всех фильмов:", average_imdb(movies))
print("\n5. Средний рейтинг категории Romance:", average_imdb_by_category(movies, "Romance"))
