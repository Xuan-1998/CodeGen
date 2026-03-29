code
from sys import stdin

def solve():
    n = int(stdin.readline())
    array = list(map(int, stdin.readline().split()))
    memo = {i: 1 for i in range(n)}
    
    for i in range(n):
        for j in range(i):
            if array[i] > array[j]:
                memo[i] = max(memo[i], memo[j] + 1)
    
    return max(memo.values())

print(solve())
