# Read input array from standard input
n = int(input())
arr = list(map(int, input().split()))

# Initialize table S with all zeros
S = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            S[i] = max(S[i], S[j] + 1)

print(max(S))
