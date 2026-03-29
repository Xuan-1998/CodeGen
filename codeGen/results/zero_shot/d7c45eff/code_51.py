import sys

def smallest_string(n, k, s):
    # Check if the string can be directly duplicated
    if k >= n:
        return s * (k // n) + s[:k % n]

    # If not, check if we need to delete the last character
    if k < n - 1:
        return s[:-1] * (k // (n - 1)) + s[:(k % (n - 1))]
    
    # If it's exactly one less than the length of the string
    else:
        if s[-1] <= s[k-1]:
            return s[:-1]
        else:
            return s

n, k = map(int, input().split())
s = input()

print(smallest_string(n, k, s))
