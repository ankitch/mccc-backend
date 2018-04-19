import random
import string

from django.conf import settings

SHORTCODE_MIN = getattr(settings, 'SHORTCODE_MIN', 6)


def short_code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
    new_code = " "
    for _ in range(size):
        new_code += random.choice(chars)

    return new_code


def create_short_code(instance, size=6):
    new_code = short_code_generator(size=size)
    print(instance.__class__.url)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(short_code=new_code).exists()
    if qs_exists:
        return short_code_generator(size=size)
    return short_code_generator(size=size)
