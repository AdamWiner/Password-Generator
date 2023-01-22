import random
import string


def generate_password(length):
    password = ''.join(random.choice(string.ascii_letters +
                       string.digits + string.punctuation) for i in range(length))
    return password


# Example usage
print(generate_password(15))
