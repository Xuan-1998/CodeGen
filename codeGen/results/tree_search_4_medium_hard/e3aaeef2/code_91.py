import sys

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [0] * (n + 1)
        for i in range(n+1):
            if m == 0:
                dp[i] = len(str(i))
            else:
                temp = list(str(i))
                for j in range(len(temp)):
                    temp[j] = str(int(temp[j]) + 1)
                dp[i] = min(dp[int(''.join(temp))], dp[i])
        print(dp[n] % (10**9 + 7))

if __name__ == "__main__":
    main()
