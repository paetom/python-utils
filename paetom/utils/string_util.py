import random

def get_random_key(size):

    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    str_rand = ""

    for i in range(size):
        str_rand += chars[random.randint(0, len(chars) - 1)]

    return str_rand
pass