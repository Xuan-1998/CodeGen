import math

def min_perfect_squares(n):
    perfect_squares = []
    i = 1
    while i * i <= n:
        perfect_squares.append(i * i)
        i += 1
    
    if sum(perfect_squares) < n:
        return -1
    
    cum_sum = 0
    num_squares = 0
    for square in perfect_squares:
        cum_sum += square
        while cum_sum > n:
            cum_sum -= square
            num_squares += 1
    
    return num_squares + 1

n = int(input())
print(min_perfect_squares(n))
