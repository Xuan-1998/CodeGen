import sys

n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()

if k > n:
    # If k is greater than the length of the string, we need to duplicate the string
    result = s * (k // n) + s[:k % n]
else:
    # If k is less than or equal to the length of the string, we can delete characters
    if k == 1:
        # If k is 1, just return the character at index k-1
        result = s[k-1]
    else:
        # Otherwise, we need to find the lexicographically smallest substring of length k
        min_str = ''
        for i in range(n-k+1):
            if s[i:i+k] < min_str or not min_str:
                min_str = s[i:i+k]
        result = min_str

print(result)
