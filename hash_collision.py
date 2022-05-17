import hashlib
import os
import random
import string


def hash_collision(k):
    print("test")
    if not isinstance(k, int):
        print("hash_collision expects an integer")
        return b'\x00', b'\x00'
    if k < 0:
        print("Specify a positive number of bits")
        return b'\x00', b'\x00'

    # Collision finding code goes here

    letters = string.ascii_letters
    x = (''.join(random.choice(letters) for i in range(random.randint(1, 10)))).encode('utf-8')
    hash_x = hashlib.sha256(x).hexdigest()

    while True:
        y = (''.join(random.choice(letters) for i in range(random.randint(1, 10)))).encode('utf-8')
        hash_y = hashlib.sha256(y).hexdigest()
        if hash_x[-k:] == hash_y[-k:] and x != y:
            break

    return x, y
