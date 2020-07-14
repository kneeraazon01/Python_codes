import sys
import os
import string
import random
print(sys.version)

def pw_gen(size=25, chars=string.ascii_letters + string.digits + string.punctuation):
    return "".join(random.choice(chars) for _ in range(size))


print(pw_gen(int(input("How many characters in your password?"))))
