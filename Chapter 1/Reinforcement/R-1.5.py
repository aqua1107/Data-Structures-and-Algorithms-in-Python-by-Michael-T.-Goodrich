#R-1.5
n = int(input().strip())
sum_of_squares_less_than_n = sum([i**2 for i in range(1, n) if i**2 < n])
print(sum_of_squares_less_than_n)
