import sys

def read_input():
    n = int(input())
    monsters = list(map(int, input().split()))
    healths = list(map(int, input().split()))
    return n, monsters, healths

def solve(n, monsters, healths):
    dp = [[0] * (monsters[-1] + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(monsters[i - 1], -1, -1):
            if i == 1:
                dp[i][j] = healths[0]
            else:
                dp[i][j] = min(dp[i-1][monsters[i-2]] + healths[i-1], dp[i][j])
    
    return dp[-1][-1]

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, monsters, healths = read_input()
        print(solve(n, monsters, healths))
