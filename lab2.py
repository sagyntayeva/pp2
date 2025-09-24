# ===========================
# PYTHON FULL NOTES & EXAMPLES
# ===========================

# ---------- Boolean Values ----------
# Boolean (bool): Data type that can be only True or False.
# True / False: Logical values representing truth or falsity.
# bool() function: Converts any value to True or False.
print(bool("Hello"))  # True because non-empty string is True
print(bool(15))       # True because any non-zero number is True

# Values considered True: any non-empty string, any non-zero number,
# any non-empty list/tuple/set/dict.
# Values considered False: empty string "", number 0, empty collections.

# ---------- Function Returning Boolean ----------
def myFunction():
    return True  # Function that returns Boolean True

if myFunction():            # if condition checks the Boolean value
    print("YES!")
else:
    print("NO!")

# isinstance(object, type): Checks if object is of a given type, returns Boolean.
x = 200
print(isinstance(x, int))    # True because x is an integer

# ---------- Operator Groups ----------
# Python operators are divided into:
# 1) Arithmetic: + - * / % ** //
# 2) Assignment: = += -= *= /= %= //= **= &= |= ^= >>= <<=
# 3) Comparison: == != > < >= <=
# 4) Logical: and or not
# 5) Identity: is, is not
# 6) Membership: in, not in
# 7) Bitwise: & | ^ ~ << >>

# ---------- Arithmetic Operators ----------
# + Addition: x + y
# - Subtraction: x - y
# * Multiplication: x * y
# / Division: x / y
# % Modulus: x % y  (remainder)
# ** Exponentiation: x ** y (x to the power y)
# // Floor division: x // y (integer division)

# ---------- Assignment Operators ----------
# =   : Assign value        x = 5
# +=  : Add and assign      x += 3   (x = x + 3)
# -=  : Subtract and assign x -= 3
# *=  : Multiply and assign x *= 3
# /=  : Divide and assign   x /= 3
# %=  : Modulus and assign  x %= 3
# //=: Floor divide assign  x //= 3
# **=: Power assign         x **= 3
# &=  : AND bitwise assign  x &= 3
# |=  : OR bitwise assign   x |= 3
# ^=  : XOR bitwise assign  x ^= 3
# >>= : Right shift assign  x >>= 3
# <<= : Left shift assign   x <<= 3
# :=  : Walrus operator     print(x := 3)  # Assign inside expression

# ---------- Comparison Operators ----------
# == : Equal
# != : Not equal
# >  : Greater than
# <  : Less than
# >= : Greater or equal
# <= : Less or equal

# ---------- Logical Operators ----------
# and : True if both conditions are True
# or  : True if at least one condition is True
# not : Negates the result
x = 5
print(x < 5 and x < 10)
print(x < 5 or x < 4)
print(not(x < 5 and x < 10))

# ---------- Identity Operators ----------
# is     : True if two variables reference the same object in memory
# is not : True if they do not reference the same object

# ---------- Membership Operators ----------
# in     : True if value is present in sequence
# not in : True if value is NOT present

# ---------- Bitwise Operators ----------
# &  : AND – bit is 1 if both bits are 1
# |  : OR  – bit is 1 if one bit is 1
# ^  : XOR – bit is 1 if only one bit is 1
# ~  : NOT – inverts bits
# << : Zero fill left shift
# >> : Signed right shift

# ---------- Lists ----------
# List: Ordered, changeable collection allowing duplicates.
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(len(thislist))  # len(): returns number of items

# List items can be of any data type and mixed types.
list1 = ["abc", 34, True, 40, "male"]
print(type(list1))  # type(): shows the type of the object

# list() constructor: creates a list
thislist = list(("apple", "banana", "cherry"))

# Negative indexing: -1 is last item, -2 is second last, etc.
# Check membership:
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# Modify items:
thislist[1] = "blackcurrant"
# Remove by value:
thislist.remove("banana")
# Remove by index:
thislist.pop(1)
# Remove last item:
thislist.pop()
# del keyword: delete by index or entire list
del thislist[0]
# Clear all items but keep list object:
thislist.clear()

# Loop through list using while:
i = 0
fruits = ["apple", "banana", "cherry"]
while i < len(fruits):
    print(fruits[i])
    i += 1

# List comprehension examples:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
newlist = [x for x in fruits if x != "apple"]
newlist = [x for x in range(10)]

# reverse(): Reverse current order
fruits.reverse()
# sort() with key:
fruits.sort(key=str.lower)

# Custom sort key:
def myfunc(n):
    return abs(n - 50)
numbers = [100, 50, 65, 82, 23]
numbers.sort(key=myfunc)

# Copy a list:
mylist = fruits.copy()
mylist2 = list(fruits)
mylist3 = fruits[:]  # slice operator

# Join lists:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
list3 = list1 + list2

# Common list methods:
# append(), clear(), copy(), count(), extend(), index(), insert(),
# pop(), remove(), reverse(), sort()

# ---------- Tuples ----------
# Tuple: Ordered, unchangeable collection, allows duplicates.
x = ("apple", "banana", "cherry")
# Convert tuple to list to modify:
y = list(x)
y[1] = "kiwi"
x = tuple(y)

# Tuple unpacking:
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

# Loop through tuple:
for item in fruits:
    print(item)

# Join tuples:
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2

# Tuple methods:
# count(): number of occurrences
# index(): position of first occurrence

# ---------- Sets ----------
# Set: Unordered, unindexed collection of unique elements.
thisset = set(("apple", "banana", "cherry"))
thisset.add("orange")
thisset.update(["kiwi", "orange"])
thisset.remove("banana")    # raises error if not found
thisset.discard("banana")   # no error if not found

# Set operations:
# union() | : all items from both sets
# intersection() & : common items
# difference() - : items in first set not in second
# symmetric_difference() ^ : items not common to both
# frozenset: immutable version of set

# Important set methods:
# add(), clear(), copy(), difference(), difference_update(),
# discard(), intersection(), intersection_update(),
# isdisjoint(), issubset(), issuperset(),
# pop(), remove(), symmetric_difference(),
# symmetric_difference_update(), union(), update()

# ---------- Dictionaries ----------
# Dictionary: Key-value pairs, ordered*, changeable, no duplicates.
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict.get("model"))  # get(): returns value of key
print(thisdict.keys())        # keys(): returns list of keys
thisdict.update({"year": 2020})  # update(): change/add key-value

# Delete operations:
del thisdict["model"]
# del thisdict deletes entire dictionary
# popitem(): removes last inserted key-value
# values(): returns list of values
for val in thisdict.values():
    print(val)
for key in thisdict.keys():
    print(key)

# Copy dictionary:
mydict = thisdict.copy()
mydict2 = dict(thisdict)

# Dictionary methods:
# clear(), copy(), fromkeys(), get(), items(), keys(),
# pop(), popitem(), setdefault(), update(), values()

# ---------- Control Statements ----------
# match statement: pattern matching similar to switch
day = 4
match day:
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case 4: print("Thursday")
    case 5: print("Friday")
    case 6: print("Saturday")
    case 7: print("Sunday")

# continue: skip current iteration
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# while loop: repeats while condition is True
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")  # else executes when loop ends normally

# break: exit loop early
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# range(): generates sequence of numbers
for x in range(6):
    print(x)
