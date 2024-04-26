n, k = map(int, input().split())
problems = list(map(int, input().split()))

solved_problems = 0

for i in range(n):
    if problems[i] <= k:
        solved_problems += 1
    else:
        break

print(solved_problems)
