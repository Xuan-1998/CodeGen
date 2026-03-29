def prob_at_least_one(s, h):
    n = sum(s)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if s[h - 1] >= i:
            dp[i] = 1.0
        else:
            p = s[h - 1] / sum(s)
            dp[i] = max(0.0, 1 - (1 - p) ** i)

    return dp[n]

def main():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    
    if n > sum(s):
        print(-1)
    else:
        print(prob_at_least_one(s, h))

if __name__ == "__main__":
    main()
