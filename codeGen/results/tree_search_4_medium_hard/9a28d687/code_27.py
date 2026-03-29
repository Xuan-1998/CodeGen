import sys
from collections import defaultdict

def solve():
    n = int(input())
    costs = list(map(int, input().split()))
    strings = [input() for _ in range(n)]
    
    dp = [[0] * (n+1) for _ in range(n+1)]
    rev_costs = [(s, c) for s, c in zip(strings, costs)]

    for i in range(1, n+1):
        last = strings[i-1]
        for j in range(i, 0, -1):
            if strings[j-1] <= last:
                dp[i][j] = min(dp[i][k]+costs[k]+costs[-1-ord(s)-1] for k in range(j))
                break
        else:
            print(-1)
            return
    print(sum(costs) - 2*sum(min(ord(c1), ord(c2)) < 0 for s1, c1 in zip(strings, costs) for s2, c2 in zip(rev_costs, [c-ord(s)-1 for s, c in rev_costs] if i > 0 else [(s, c) for s, c in zip(strings, costs)]))

if __name__ == "__main__":
    solve()
