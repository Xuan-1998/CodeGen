# Step 1: Read input
n, k = map(int, input().split())
s = input()

# Step 2: Check if k is larger than n
if k > n:
    # If k is larger than n, then we need to duplicate the string until it reaches length k
    s *= (k // n) + (1 if k % n != 0 else 0)
    # Now check if the last character of the string needs to be deleted
    if k % n > 0:
        s = s[:-1]
