n = int(input())
total_sum = sum(int(x) for x in input().split())

left_sum = 0
count = 0
for num in input().split():
    left_sum += int(num)
    if left_sum == total_sum // 2:
        count += 1
    elif left_sum > total_sum // 2:
        break

print(count)
