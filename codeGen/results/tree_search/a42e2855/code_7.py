def main():
    T = int(input().strip())
    for _ in range(T):
        N, P = map(int, input().split())
        dp = [0.0] * (N+1)
        dp[0] = 1.0

        for i in range(1, N+1):
            if i - 2 >= 0:
                dp[i] += dp[i-2] * (P/100)
            if i - 3 >= 0:
                dp[i] += dp[i-3] * ((100-P)/100)
        
        print(f'{dp[N]:.6f}')

if __name__ == "__main__":
    main()
