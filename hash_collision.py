import hashlib
import os
import random
import string


def hash_collision(k):
    if not isinstance(k, int):
        print("hash_collision expects an integer")
        return b'\x00', b'\x00'
    if k < 0:
        print("Specify a positive number of bits")
        return b'\x00', b'\x00'

    # Collision finding code goes here

    mask = int(''.join(['0' for i in range(256 - k)] + ['1' for i in range(k)]), 2)

    letters = string.ascii_letters
    x = (''.join(random.choice(letters) for i in range(random.randint(1, 10)))).encode('utf-8')
    hash_x = hashlib.sha256(x).hexdigest()
    comp_x = int(hash_x, 16) & mask

    while True:
        y = (''.join(random.choice(letters) for i in range(random.randint(1, 10)))).encode('utf-8')
        hash_y = hashlib.sha256(y).hexdigest()
        comp_y = int(hash_y, 16) & mask
        if comp_x == comp_y and x != y:
            break

    return x, y
