def min_cuts(s):
    n = len(s)
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    # Initialize the base case: an empty string is a palindrome
    dp[0][0] = True

    for i in range(n + 1):
        for j in range(i, -1, -1):
            if s[j] == s[i]:
                if i - j <= 2 or dp[j][i - 1]:
                    dp[j][i] = True
            else:
                # Check the three cases you mentioned
                dp[j][i] = (dp[j + 1][i - 1] and s[j] == s[i]) or \
                           (dp[j + 1][i - 1] and j >= i - 1) or \
                           (j <= i - 2 and not dp[j + 1][i - 1])

    # Find the minimum number of cuts
    cuts = float('inf')
    for i in range(1, n):
        if not dp[0][i]:
            cuts = min(cuts, i)
            break

    return cuts


def main():
    s = input().strip()
    print(min_cuts(s))


if __name__ == "__main__":
    main()
