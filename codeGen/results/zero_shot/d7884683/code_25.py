n = int(input())
left_sum = 0
right_sum = sum(input().split()) - left_sum
max_count = 0
count = 0

while right_sum != left_sum:
    if right_sum > left_sum:
        right_sum -= input().split()[0]
    else:
        left_sum += input().split()[0]
    count += 1

print(count)
