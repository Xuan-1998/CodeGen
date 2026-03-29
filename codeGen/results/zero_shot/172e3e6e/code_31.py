# Read the input
n = int(input())
a = list(map(int, input().split()))

# Initialize the count of good subsequences
count = 0

# Iterate over each element in the array
for i in range(1, n + 1):
    # Check if the current element is divisible by its index
    if a[i - 1] % i == 0:
        # If it is, increment the count
        count += 1

print(count)
