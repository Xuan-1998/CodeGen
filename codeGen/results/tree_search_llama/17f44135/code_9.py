n, k = map(int, input().split())
problems = list(map(int, input().split()))
current_diff = problems[0]
left_solved = 1 if current_diff <= k else 0
right_solved = 1 if current_diff <= k else 0

max_solved = left_solved + right_solved

for i in range(1, n-1):
    if problems[i] <= k:
        max_solved += 1
    elif problems[n-i-1] <= k:
        max_solved += 1
    current_diff = min(problems[i], problems[n-i-1])

print(max_solved)
