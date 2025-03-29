#C-1.15
def isdistinct(data):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i] == data[j]:
                return False
    return True