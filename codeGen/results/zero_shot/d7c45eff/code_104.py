# Step 1: Read input
n, k = map(int, input().split())
s = input()

# Step 2: Check if string length is already equal to k
if n == k:
    print(s)
    exit()
