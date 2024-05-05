def is_palindrome(s):
    return s == s[::-1]

def min_cuts(s):
    n = len(s)
    dp = [n] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for j in range(i):
            if is_palindrome(s[j:i]):
                dp[i] = min(dp[i], dp[j] + 1)

    return dp[-1]

if __name__ == "__main__":
    s = input()
    print(min_cuts(s))
