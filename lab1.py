# =================================================
# PYTHON BASICS  (based on W3Schools)
# Topics: Python Syntax → Comments → Variables → Data type → Numbers → Strings
# =================================================


# -------------------------------------------------
# RUN PYTHON SYNTAX
# -------------------------------------------------
# Run in command line:
#   print("Hello, World!")
# Or create a file with .py extension (e.g. myfile.py) and run:
#   python myfile.py


# -------------------------------------------------
# INDENTATION
# -------------------------------------------------
# Indentation defines code blocks. Missing or inconsistent indentation = Error.

if 5 > 2:
    print("Five is greater than two!")   # correct

# Wrong (no indentation):
# if 5 > 2:
# print("Five is greater than two!")     # error

# Any number of spaces is allowed if consistent:
if 5 > 2:
        print("Still works, but not recommended style")


# -------------------------------------------------
# COMMENTS
# -------------------------------------------------
# This is a comment
print("Hello, World!")   # comment can explain code or disable execution


# -------------------------------------------------
# VARIABLES
# -------------------------------------------------
# Created when assigning a value.
x = 5
y = "Hello, World!"
print(x)
print(y)

# Dynamic typing – no need to declare in advance
x = str(3)     # '3'
y = int(3)     # 3
z = float(3)   # 3.0

x = 5
y = "John"
print(type(x))   # int
print(type(y))   # str

# Valid variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Unpacking a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Local vs Global variables
x = "awesome"
def myfunc():
    x = "fantastic"           # local variable
    print("Python is " + x)
myfunc()
print("Python is " + x)       # global variable unchanged


# -------------------------------------------------
# DATA TYPES – examples
# -------------------------------------------------
# str, int, float, complex, list, tuple, range, dict, set, frozenset, bool, bytes, bytearray, memoryview
x = str("Hello World")              # str
x = int(20)                         # int
x = float(20.5)                      # float
x = complex(1j)                      # complex
x = list(("apple", "banana"))        # list
x = tuple(("apple", "banana"))       # tuple
x = range(6)                         # range
x = dict(name="John", age=36)        # dict
x = set(("apple", "banana"))         # set
x = frozenset(("apple", "banana"))   # frozenset
x = bool(5)                          # bool
x = bytes(5)                         # bytes
x = bytearray(5)                      # bytearray
x = memoryview(bytes(5))             # memoryview

x = 1    # int
y = 2.8  # float
z = 1j   # complex


# -------------------------------------------------
# STRINGS
# -------------------------------------------------
# Single or double quotes:
a = "Hello"
b = 'World'
print(a)
print(b)

# Multi-line
multi_line = """This is a string
that spans
multiple lines."""
print(multi_line)

# Escaping
quote = "He said: \"Hello!\""
print(quote)

# Concatenation
s1 = "Hello, "
s2 = "World!"
s = s1 + s2
print(s)

# f-string formatting
name = "Anna"
age = 25
formatted = f"My name is {name}, and I am {age} years old."
print(formatted)

# Useful methods
a = " Hello, World! "
print(a.strip())   # remove whitespace
print(a.lower())   # lower case
print(a.upper())   # upper case

# Escape sequences
# \'  Single Quote
# \\  Backslash
# \n  New Line
# \r  Carriage Return
# \t  Tab
# \b  Backspace
# \f  Form Feed
# \ooo Octal value
# \xhh Hex value


# =================================================
# GIT BASICS
# =================================================
# Git repository — a storage of your project and its history (.git folder is hidden).
# Branch — parallel version of the repository to work independently.


# -------------------------------------------------
# COMMON COMMANDS
# -------------------------------------------------
git_init          = "git init – create an empty Git repository in the current folder"
git_status        = "git status – show state of working directory and staging area"
git_add           = "git add <file> – add changes to the staging area"
git_commit_m      = 'git commit -m "message" – record staged changes with a message'
git_log           = "git log – show commit history (most recent first)"
git_diff          = "git diff – show unstaged changes vs last commit"
git_diff_staged   = "git diff --staged – show staged changes not yet committed"

# -------------------------------------------------
# MOVING THROUGH HISTORY
# -------------------------------------------------
git_checkout_commit = "git checkout <commit_hash> – switch to a specific commit (detached HEAD)"
git_checkout_branch = "git checkout <branch> – switch to another branch"
git_branch          = "git branch – list, create, or delete branches"

# -------------------------------------------------
# WORKING WITH FILES
# -------------------------------------------------
git_rm = "git rm <file> – remove file and stage the deletion"
git_mv = "git mv <old> <new> – rename or move file and stage change"

# -------------------------------------------------
# UNDOING CHANGES
# -------------------------------------------------
git_restore_staged = "git restore --staged <file> – unstage changes but keep edits"
git_restore_file   = "git restore <file> – discard working directory changes"
git_reset_soft     = "git reset --soft <commit> – move HEAD, keep changes staged"
git_reset_mixed    = "git reset --mixed <commit> – move HEAD, unstage changes"
git_reset_hard     = "git reset --hard <commit> – move HEAD, discard all changes"

# -------------------------------------------------
# EXAMPLE WORKFLOW (Lesson 13 context)
# -------------------------------------------------
#   1. git init
#   2. git add .
#   3. git commit -m "Initial commit"
#   4. git branch feature
#   5. git checkout feature
#   6. work, commit
#   7. git checkout main
#   8. git merge feature
