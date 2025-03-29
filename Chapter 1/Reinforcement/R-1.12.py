#R-1.12
import random

def my_choice(data):
    if not data:
        raise IndexError("Cannot choose from an empty sequence")

    index = random.randrange(len(data))
    return data[index]
