#R-1.3
def minmax(data):
    maximum = data[0]
    minimum = data[0]
    for i in data:
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i
    return maximum, minimum