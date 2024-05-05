n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

tasks = []
for _ in range(k):
    l, r = map(int, input().split())
    tasks.append((l, r))

for l, r in tasks:
    for j in range(m):
        column = [row[j] for row in table[l-1:r]]
        if not is_sorted(column):
            print("No")
            break
    else:
        print("Yes")

def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
