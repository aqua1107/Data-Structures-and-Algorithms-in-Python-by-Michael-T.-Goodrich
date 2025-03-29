#C-1.14
def odd_product(data):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] % 2 != 0 and data[j] % 2 != 0:
                return True
    return False