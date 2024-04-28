n = int(input())
nums = list(map(int, input().split()))
count = 0
max_len = 0
for i in range(n):
    if nums[i] == 1:
        count += 1
        max_len = max(max_len, count)
    else:
        count = 0
print(max_len)
