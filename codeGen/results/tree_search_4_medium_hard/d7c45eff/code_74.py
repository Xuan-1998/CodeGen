from collections import defaultdict

def dp(s, i, dup):
    if i >= k:
        return s

    memo = defaultdict(lambda: default_tuple)

    def delete_last_char():
        # Delete the last character of the string
        return dp(s[:-1], i-1, False)

    def duplicate_string():
        # Duplicate the original string
        return dp(s + s[-1], i+1, True)

    if dup:
        return duplicate_string()
    elif i < n-1:
        return min(delete_last_char(), duplicate_string())
    else:
        return duplicate_string()

n, k = map(int, input().split())
s = input().strip()

result = dp(s, 0, False)
print(result)
