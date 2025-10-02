class first:
    def __init__(self):
        self.s = ""

    def get(self):
        self.s = input("your string: ")

    def print(self):
        print(self.s.upper())


obj = first()
obj.get()
obj.print()

#task2

class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length



shape = Shape()
print("Shape area:", shape.area())

length = int(input("length:"))
square = Square(length)
print("Square area:", square.area())

#task3
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width



length = int(input("the length : "))
width = int(input(" the width: "))

rect = Rectangle(length, width)
print("rectangle area:", rect.area())

#task4
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)



p1 = Point(3, 4)
p2 = Point(0, 0)

p1.show()
p2.show()

print("Distance between points:", p1.dist(p2))

p1.move(7, 1)
p1.show()
print("New distance:", p1.dist(p2))

#task5

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds! Withdrawal denied.")

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance}"


name = input("Enter account owner's name: ")
acc = Account(name, 0)
print(acc)

while True:
    action = input("\nChoose action (deposit / withdraw / show / exit): ").lower()

    if action == "deposit":
        amount = int(input("Enter amount to deposit: "))
        acc.deposit(amount)

    elif action == "withdraw":
        amount = int(input("Enter amount to withdraw: "))
        acc.withdraw(amount)

    elif action == "show":
        print(acc)

    elif action == "exit":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid action! Try again.")

#task6

class PrimeFilter:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_primes(self):
        return list(filter(lambda x: self.is_prime(x), self.numbers))


nums = list(map(int, input("numbers").split()))
pf = PrimeFilter(nums)
print( pf.get_primes())

