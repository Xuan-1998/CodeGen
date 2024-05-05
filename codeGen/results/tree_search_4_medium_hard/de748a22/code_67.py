import sys

def solve():
    n, q = map(int, input().split())
    signs = list(input())

    dp = [[0]*(n+1) for _ in range(n+1)]
    
    cumulative_sum = 0
    sign_counts = [0]
    for i in range(1, n+1):
        cumulative_sum += 1 if signs[i-1] == '-' else -1
        sign_counts.append(cumulative_sum)
    
    for l in range(1, n+1):
        for r in range(l, n+1):
            if sign_counts[r]-sign_counts[l-1] > 0:
                dp[l][r] = r-l+1
            elif sign_counts[r]-sign_counts[l-1] < 0:
                dp[l][r] = l-1
            else:
                for i in range(l, r+1):
                    if sign_counts[i]-sign_counts[l-1] == 0:
                        dp[l][r] = min(dp[l][i]+(r-i), i-l+1)
                        break
    
    for _ in range(q):
        l, r = map(int, input().split())
        print(min(dp[l][r], key=lambda x: (x, r-l+1)))

if __name__ == "__main__":
    solve()
