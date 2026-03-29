# Step 1: Understand the problem
print("Problem understood!")

# Step 2: Clarify the input format
n, k = map(int, input().split())
s = input()

# Step 3: Identify the key operation
if k <= n:
    # If the original string is long enough, delete the last character if possible
    if k < n:
        result = s[:-1]
    else:
        result = s
else:
    # If the desired length is longer than the original string, duplicate it
    result = s * (k // n) + (s[:k % n] if k % n != 0 else '')

print(result)
