import sys

def min_recolors(colors):
    n = len(colors)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if colors[i - 1] == 'R':
            dp[i] = dp[i - 1] + (dp[i - 2] if i >= 2 else 0)
        elif colors[i - 1] == 'G':
            dp[i] = dp[i - 1] + (dp[i - 2] if i >= 2 and colors[i - 2] == 'R' else 0)
        else:
            dp[i] = dp[i - 1] + (dp[i - 2] if i >= 2 and colors[i - 2] in ['R', 'G'] else 0)

    return dp[-1]

def main():
    n = int(input())
    colors = input()

    print(min_recolors(colors))

if __name__ == "__main__":
    main()
