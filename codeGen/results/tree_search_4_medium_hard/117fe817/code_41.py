import math

def findCount(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        total_ones = dp[i - 1]
        ones_in_i = floor(log2(i))
        dp[i] = total_ones + ones_in_i
    return dp[n]

def main():
    n = int(input())
    print(findCount(n))

if __name__ == "__main__":
    main()
