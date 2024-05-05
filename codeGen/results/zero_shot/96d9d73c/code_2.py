import sys

N, K, M = map(int, input().split())
A = list(map(int, input().split()))

# Sort the array
A.sort()

left = 0
right = N - 1

while left < right:
    if A[right] - A[left] <= M:
        left += 1
    else:
        right -= 1

if (right - left + 1) >= K:
    print("True")
else:
    print("False")
