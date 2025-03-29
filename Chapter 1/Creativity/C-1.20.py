#C-1.20
import random

def my_shuffle(data):

    n = len(data)
    
    for i in range(n-1, 0, -1):
        j = random.randint(0, i)
        data[i], data[j] = data[j], data[i]