from collections import Counter

def count_ones(n):
    ones = [str(i).count('1') for i in range(n+1)]
    return sum(ones)

n = int(input())
print(count_ones(n))
