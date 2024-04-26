n, k = map(int, input().split())
problems = list(map(int, input().split()))
problems.sort()

count = 0
leftmost = rightmost = None

for i in range(len(problems)):
    if problems[i] <= k:
        count += 1
        leftmost = min(leftmost, problems[i]) if leftmost is not None else problems[i]
        rightmost = max(rightmost, problems[i])

while leftmost and rightmost and (rightmost - leftmost) <= k:
    count += 2
    problems.pop(0)
    problems.pop()
    leftmost = min(problems) if problems else None
    rightmost = max(problems) if problems else None

print(count)
