n = int(input())
nums = list(map(int, input().split()))
max_len = 0
cur_len = 0
for num in nums:
    if num == 1:
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 0
print(max_len-1)
