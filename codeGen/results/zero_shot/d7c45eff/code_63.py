# Read input
n, k = map(int, input().split())
s = input()

# Initialize result string
result = ""

# Check if k is greater than or equal to n
if k >= n:
    # If k is greater than or equal to n, duplicate the string s until we reach length k
    for _ in range((k - n) // n + 1):
        result += s
else:
    # If k is less than n, just take the first k characters of string s
    result = s[:k]

print(result)
