def main():
    t, l, r = map(int, input().split())
    dp = [0] * (r + 1)
    
    for i in range(2, r + 1):
        dp[i] = dp[i - 1] + 1
    
    result = sum((t // i) * dp[i] for i in range(l, r + 1))
    print(result % (10**9 + 7))

if __name__ == "__main__":
    main()
