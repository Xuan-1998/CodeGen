n, k = map(int, input().split())
a = list(map(int, input().split()))

left_solved, right_solved = 0, 0

for i in range(n):
    if a[i] <= k:
        left_solved += 1
    if i > 0 and a[n-i-1] <= k:
        right_solved += 1

max_solved = max(left_solved, right_solved)

print(max_solved)
