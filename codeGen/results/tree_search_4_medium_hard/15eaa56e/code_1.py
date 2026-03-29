def is_sorted(subtable):
    for i in range(len(subtable) - 1):
        for j in range(1, len(subtable[0])):
            if subtable[i][j] > subtable[i + 1][j]:
                return False
    return True

def solve():
    n, m = map(int, input().split())
    table = [[*map(int, input().split())] for _ in range(n)]
    k = int(input())
    tasks = [list(map(int, input().split())) for _ in range(k)]

    for task in tasks:
        l, r = task
        subtable = [row[l:r + 1] for row in table]
        if is_sorted(subtable):
            print("Yes")
        else:
            print("No")

