import sys

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        monsters = []
        for i in range(n):
            k, h = map(int, input().split())
            monsters.append((k, h))
        
        dp = {0: 1}
        for i in range(1, n+1):
            min_mana = float('inf')
            for j in range(1, i+1):
                if j >= monsters[i-1][1]:
                    min_mana = min(min_mana, dp.get(j-1, float('inf')) + 1)
            dp[i] = min_mana
        
        print(dp[n])

if __name__ == "__main__":
    solve()
