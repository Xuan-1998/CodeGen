import sys

def main():
    n, m = map(int, input().split())
    plants = list(map(lambda x: (int(x.split()[1]), int(x.split()[0])), [input().split() for _ in range(n)]))

    dp = [[0] * m for _ in range(n + 1)]
    for i in range(1, n + 1):
        section = plants[i - 1][0]
        prev_section = (i - 1) // (m - 1)
        if plants[i - 1][1] <= (prev_section + 1) * m:
            dp[i][section - 1] = min(dp[i - 1][section - 1], dp[i - 1][prev_section] + 1)
        else:
            dp[i][section - 1] = min(dp[i - 1][section - 1], dp[i - 1][section])

    print(min(dp[-1]))

if __name__ == "__main__":
    main()
