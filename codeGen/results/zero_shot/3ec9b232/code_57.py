# Take input
n = int(input())

# Initialize an array to store the frequency of each element
freq = [0] * (n + 1)

# Read the array M
M = list(map(int, input().split()))
for m in M:
    freq[m] += 1

# Calculate the number of ways to create a collection V
ans = 1
for i in range(1, n + 1):
    ans *= comb(n - 1, freq[i] - 1)
    if freq[i] > 0:
        ans //= (freq[i] + 1)

print(ans % (10**9 + 7))
