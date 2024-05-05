import sys

def solve(n, k):
    s = input().strip()
    if k <= n:
        # If k is less than or equal to n, we can delete the last character
        result = s[:k]
    else:
        # If k is greater than n, we need to duplicate the string and then take the first k characters
        result = (s + s)[:k]

    return result

n, k = map(int, input().split())
print(solve(n, k))
