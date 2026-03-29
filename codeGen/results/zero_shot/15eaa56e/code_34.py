def is_sorted_column(column):
    for i in range(1, len(column)):
        if column[i - 1] > column[i]:
            return False
    return True

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

for _ in range(k):
    l, r = map(int, input().split())
    for j in range(m):
        column = [row[j] for row in table[l - 1:r]]
        if is_sorted_column(column):
            print("Yes")
            break
    else:
        print("No")
