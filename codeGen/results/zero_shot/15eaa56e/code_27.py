import sys

def is_sorted_subtable(table, n, m, k):
    for _ in range(k):
        l, r = map(int, input().split())
        for j in range(m):
            column = [row[j] for row in table[l-1:r]]
            if not all(column[i] <= column[i+1] for i in range(len(column)-1)):
                return "No"
    return "Yes"

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

print(is_sorted_subtable(table, n, m, k))
