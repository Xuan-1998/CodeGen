# Read the input
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

# Sort the array A in ascending order
A.sort()

# Initialize two pointers for the partition
left = 0
right = 0

while right < N:
    if A[right] - A[left] <= M:
        right += 1
    else:
        left += 1
        if right - left >= K:
            print(True)
            break
else:
    print(False)
