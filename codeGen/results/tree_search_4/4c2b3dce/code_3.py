import sys

def check_string(s):
    dp = [False] * (len(s) + 1)
    for i in range(len(s)):
        if s[i:i+2] == 'AB' or s[i:i+2] == 'BA':
            dp[i + 1] = True
        if i >= 2 and dp[i - 1]:
            if s[i-1:i+1] == 'BA':
                dp[i] = True
    return "YES" if dp[-1] else "NO"

if __name__ == "__main__":
    s = input()
    print(check_string(s))
