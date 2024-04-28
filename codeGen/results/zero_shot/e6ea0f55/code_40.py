import sys
read = lambda: map(int, sys.stdin.readline().split())
n, k = read()
arr = []
for _ in range(n):
    arr.append(read()[0])
max_sum = float('-inf')
curr_sum = 0
left = 0
right = 0
while right < n:
    curr_sum += arr[right]
    while right - left > k:
        curr_sum -= arr[left]
        left += 1
    max_sum = max(max_sum, curr_sum)
    right += 1
print(max_sum)
