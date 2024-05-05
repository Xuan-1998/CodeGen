n, m = map(int, input().split())
table = [[int(x) for x in input().split()] for _ in range(n)]
k = int(input())
tasks = []
for _ in range(k):
    l, r = map(int, input().split())
    tasks.append((l, r))

def is_sorted(subtable):
    for i in range(1, len(subtable)):
        if subtable[i-1] > subtable[i]:
            return False
    return True

for l, r in tasks:
    subtable = [row[l-1:r] for row in table]
    if any(not is_sorted(column) for column in zip(*subtable)):
        print("No")
        break
else:
    print("Yes")
