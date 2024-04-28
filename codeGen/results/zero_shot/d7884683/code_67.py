n = int(input())
total_sum = sum(map(int, input().split()))
left_sum = 0
count = 0
for i in range(n):
    left_sum += map(int, input().split())[i]
    if left_sum == total_sum - left_sum:
        count += 1
print(count)
