#R-1.6
def odd_squared(n):
    result = []
    for i in range(n):
        if i % 2 == 1 and i**2 < n:
            result.append(i**2)
    return sum(result)

print(odd_sqaured(5))