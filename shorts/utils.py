import random
import string

letters = string.ascii_letters + string.digits


def generate_random_key(length=8):
    return "".join(random.choice(letters) for _ in range(length))
