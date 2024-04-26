n, k = map(int, input().split())
problems = sorted(map(int, input().split()), reverse=True)

max_solved = 0
for problem in problems:
    if problem <= k:
        max_solved += 1
    else:
        break

print(max_solved)
