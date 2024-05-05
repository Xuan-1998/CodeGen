# Read input
n, k = map(int, input().split())
s = input()

# Initialize the result string
result = ''

# Check if k is greater than or equal to n
if k >= n:
    # If k is greater than or equal to n, we need to duplicate the string 'k-n' times and remove the last character of the remaining part
    for _ in range(k // n):
        result += s
    # Remove the last character if there's a remainder
    result += s[:k % n]
else:
    # If k is less than n, we need to duplicate the string 'n-k' times and remove the last character of the remaining part
    for _ in range(n - k):
        result = s + s[:-1][::-1]
    # Remove the last character if there's a remainder
    result += s[-k:]

# Print the result
print(result)
