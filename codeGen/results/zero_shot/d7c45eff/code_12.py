# Read input
n, k = map(int, input().split())
s = input().lower()

# Check if k is greater than or equal to n
if k >= n:
    # If k is greater than or equal to n, just duplicate the string
    print(s * (k // n) + s[:k % n])
else:
    # If k is less than n, check if the last character of the string should be included
    if s[k-1] <= s[n-1]:
        # If the last character is smaller or equal to the nth character, just delete the last character
        print(s[:-1] * (k // (n - 1)) + s[:k % (n - 1)])
    else:
        # If the last character is larger than the nth character, duplicate the string up to the kth character and then add the last character
        print(s[:k-1] * (k // n) + s[k-1])
