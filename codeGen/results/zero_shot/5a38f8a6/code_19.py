import math

def min_perfect_squares(n):
    count = 0
    sum = 0
    for i in range(int(math.sqrt(n)), 0, -1):
        while sum + i <= n:
            sum += i
            count += 1
    return count

n = int(input())
print(min_perfect_squares(n))
