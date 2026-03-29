def count_arrays(n, k):
    max_and = (1 << k) - 1
    dp = [0] * (k + 1)
    dp[0] = 1
    
    for i in range(k, -1, -1):
        if (1 << i) & max_and > 0:
            max_and ^= (1 << i)
            dp[i] = sum(dp[j] for j in range(i)) + 1
        else:
            max_and &= ((1 << i) - 1)
            dp[i] = sum(dp[j] for j in range(i))
    
    return (dp[0] * pow(2, k, 10**9+7)) % (10**9+7)

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        result = count_arrays(n, k)
        print(result)

if __name__ == "__main__":
    main()
