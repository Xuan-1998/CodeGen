import sys
from io import StringIO
from functools import lru_cache

def solve():
    n = int(input())
    costs = list(map(int, input().split()))
    strings = [input() for _ in range(n)]
    
    @lru_cache(None)
    def min_cost(j):
        if j < 0:
            return float('inf')
        if j == 0:
            return 0
        
        minc = sys.maxsize
        for i in range(len(strings)):
            k = len(strings[i]) - 1
            while k >= 0 and k <= j:
                if strings[i][k:] < strings[(i+1)%n][:j-k]:
                    minc = min(minc, costs[i] + min_cost(k))
                k -= 1
        
        return minc
    
    print(min_cost(len(max(strings, key=len))))

if __name__ == "__main__":
    solve()
