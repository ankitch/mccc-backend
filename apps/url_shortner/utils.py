import random
import string


def short_code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    new_code = " "
    for _ in range(size):
        new_code += random.choice(chars)

    return new_code


def create_short_code(instance, size=6):
    new_code = short_code_generator(size=size)
