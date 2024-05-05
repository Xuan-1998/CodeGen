# Read input
n, k = map(int, input().split())
s = input()

# Check if k is greater than n
if k > n:
    # If k is greater than n, we need to duplicate s until its length reaches k
    while k > n:
        s += s  # Duplicate the string s until its length reaches k
        n = len(s)  # Update the value of n

# Check if the last character of the string needs to be removed
if k == n and s[-1] != min(s):  # If k is equal to n and the last character is not the smallest in the string
    s = s[:-1]  # Remove the last character from the string

# Print the result
print(s)
