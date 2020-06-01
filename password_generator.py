import string
import random
import sys

# password is 12 characters long
# two options:
#   1) restricted: password contains uppercase letter, lowercase letter, number, and symbol
#   2) random: password is random

PASS_LEN = 12
pwd = ""

if len(sys.argv) != 2:
    print("invalid number of arguments")
    print(str(len(sys.argv)))
    exit(1)

if sys.argv[1] == "random":
    for i in range(PASS_LEN):
        type = random.randint(0, 3)
        if type == 0:
            pwd = pwd + random.choice(string.ascii_uppercase)
        elif type == 1:
            pwd = pwd + random.choice(string.ascii_lowercase)
        elif type == 2:
            pwd = pwd + random.choice(string.digits)
        else:
            pwd = pwd + random.choice(string.punctuation)
    print(pwd)

elif sys.argv[1] == "restricted":
    chars = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    num = random.randint(0, 11)
    uppercase_index = chars[num]
    chars.pop(num)
    num = random.randint(0, 10)
    lowercase_index = chars[num]
    chars.pop(num)
    num = random.randint(0, 9)
    number_index = chars[num]
    chars.pop(num)
    num = random.randint(0, 8)
    symbol_index = chars[num]
    chars.pop(num)
    for i in range(PASS_LEN):
        if i == uppercase_index:
            pwd = pwd + random.choice(string.ascii_uppercase)
            pass
        elif i == lowercase_index:
            pwd = pwd + random.choice(string.ascii_lowercase)
            pass
        elif i == number_index:
            pwd = pwd + random.choice(string.digits)
            pass
        elif i == symbol_index:
            pwd = pwd + random.choice(string.punctuation)
        else:
            type = random.randint(0, 3)
            if type == 0:
                pwd = pwd + random.choice(string.ascii_uppercase)
            elif type == 1:
                pwd = pwd + random.choice(string.ascii_lowercase)
            elif type == 2:
                pwd = pwd + random.choice(string.digits)
            else:
                pwd = pwd + random.choice(string.punctuation)
    print(pwd)

else:
    print("invalid option")
    exit(1)