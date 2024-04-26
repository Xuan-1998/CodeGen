MOD = 998244353

def main():
    n = int(input())
    elements = [input().split() for _ in range(n)]
    
    # dp[i][j] will hold the number of ways to achieve a sum of j using the first i elements
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i, (sign, x_str) in enumerate(elements, start=1):
        if sign == "+":
            x = int(x_str)
            # Update dp for the case where x is included
            for j in range(i, 0, -1):
                for k in range(n):
                    dp[j][k + x] = (dp[j][k + x] + dp[j - 1][k]) % MOD
            # Update dp for the case where x is not included
            for j in range(i + 1):
                for k in range(n):
                    dp[j][k] = (dp[j][k] + dp[j][k]) % MOD
        else:
            # If the element is "-", just copy the previous values
            for j in range(i + 1):
                for k in range(n):
                    dp[j][k] = (dp[j][k] * 2) % MOD
    
    # Calculate the result
    result = 0
    for x_str in [x for sign, x in elements if sign == "+"]:
        x = int(x_str)
        for j in range(1, n + 1):
            result = (result + dp[j][x] * x) % MOD
    
    print(result)

if __name__ == "__main__":
    main()
