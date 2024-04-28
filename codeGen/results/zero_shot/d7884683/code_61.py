n = int(input())
for _ in range(n):
    s = list(map(int, input().split()))
    left_sum = 0
    right_sum = sum(s)
    count = 1
    for i in range(len(s)):
        left_sum += s[i]
        right_sum -= s[i]
        if left_sum == right_sum:
            count += 1
    print(count)
