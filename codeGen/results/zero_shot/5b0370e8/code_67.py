import sys
from collections import defaultdict

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        count_and = 0
        count_xor = 0
        for num in arr:
            if bin(num).count('1') == 0:
                count_and += 1
            else:
                count_xor += 1
        print((count_and * (count_xor + 1)) % (10**9 + 7))

solve()
