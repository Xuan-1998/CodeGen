import sys

def read_input():
    n, m = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(n)]
    k = int(input())
    tasks = []
    for _ in range(k):
        l, r = map(int, input().split())
        tasks.append((l-1, r-1))
    return n, m, table, k, tasks

def is_sorted_column(column):
    return all(table[i][j] <= table[i+1][j] for i in range(len(column)-1))

n, m, table, k, tasks = read_input()

for task in tasks:
    l, r = task
    subtable = [row[j] for j in range(m) for row in table[l:r+1]]
    if any(is_sorted_column([subtable[i] for i in range(len(subtable))])):
        print("Yes")
        break
else:
    print("No")
