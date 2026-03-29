# Step 1: Read the input
n, k = map(int, input().split())
s = input()

# Step 2: Check if the desired string length is larger than the original string length
if k > n:
    # If so, duplicate the original string until we reach the desired length
    s *= (k // n) + (1 if k % n != 0 else 0)

# Step 3: If the last character of the string is smaller than all other characters, remove it
if len(s) > 1 and s[-1] <= min(s[:-1]):
    s = s[:-1]

# Step 4: Print the answer
print(s)
