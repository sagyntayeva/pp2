from my_functions import sphere_volume, is_palindrome, filter_prime, guess_number


r = float(input("r: "))
print(sphere_volume(r))


word = input("word: ")
print(is_palindrome(word))


nums = list(map(int, input("numbers ").split()))
print(filter_prime(nums))


name = input("\nHello! What is your name? ")
guess_number(name)



