# Define input variables
n, k = map(int, input().split())
s = input()

# Check if k is greater than n
if k > n:
    # If k is greater than n, we need to duplicate the string s until it reaches length k
    s *= (k // n) + 1

# If k is less than or equal to n, we just need to truncate the last character of the string if necessary
if k < n:
    s = s[:-1]

# Print the result
print(s)
