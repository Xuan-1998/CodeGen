n = int(input())
left_sum = 0
count = 0
for i in range(n):
    left_sum += int(input())
    if left_sum * 2 == sum(map(int, input().split())):
        count += 1
print(count)
