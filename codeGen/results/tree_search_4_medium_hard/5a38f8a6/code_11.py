import math

def read_input():
    return int(input())

def solve(n):
    dp = {0: 0}
    for i in range(1, n + 1):
        if math.isqrt(i) ** 2 == i:
            dp[i] = 1
        else:
            min_count = float('inf')
            for j in range(math.isqrt(i) + 1):
                if j ** 2 <= i:
                    count = 1 + dp.get(i - j ** 2, float('inf'))
                    if count < min_count:
                        min_count = count
            dp[i] = min_count
    return dp[n]

def main():
    n = read_input()
    print(solve(n))

if __name__ == "__main__":
    main()
