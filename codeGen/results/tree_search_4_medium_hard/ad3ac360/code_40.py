@functools.lru_cache(None)
def is_palindrome(s):
    return s == s[::-1]

def min_cuts_to_palindromize(s):
    n = len(s)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        for j in range(i):
            if is_palindrome(s[j:i]):
                dp[i] = min(dp[i], dp[j])
            else:
                dp[i] = min(dp[i], dp[j] + 1)

    return dp[-1]

if __name__ == "__main__":
    s = input()
    print(min_cuts_to_palindromize(s))
