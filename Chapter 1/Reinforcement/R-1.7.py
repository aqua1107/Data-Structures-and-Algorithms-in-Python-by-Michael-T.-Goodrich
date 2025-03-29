#R-1.7
n = int(input().strip())
sum_of_odd_squares_less_than_n = sum([i**2 for i in range(1, n) if i**2 < n and i % 2 == 1])
print(sum_of_odd_squares_less_than_n)