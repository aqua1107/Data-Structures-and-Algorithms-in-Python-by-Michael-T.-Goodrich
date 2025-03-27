#R-1.4
def square_smaller(n):
    squared_list = []
    for i in range(1, n):
        if i**2 < n:
            squared_list.append(i**2)
    return sum(squared_list)