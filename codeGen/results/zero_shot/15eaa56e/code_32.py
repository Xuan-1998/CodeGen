def solve():
    n, m = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(n)]
    k = int(input())

    def is_sorted_subtable(l, r):
        for j in range(m):
            column = [row[j] for row in table[l-1:r]]
            if column != sorted(column):
                return False
        return True

    for task in [list(map(int, input().split())) for _ in range(k)]:
        l, r = task
        if is_sorted_subtable(l, r+1):
            print("Yes")
            return
    print("No")

solve()
