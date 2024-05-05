import sys

# Read input
n, m = map(int, input().split())
rows = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

memo = {}

def check_sorted(subtable):
    if len(subtable) <= 1:
        return True
    sorted_cols = set()
    for i in range(len(subtable[0])):
        col = tuple(row[i] for row in subtable)
        if col not in memo:
            memo[col] = all(a <= b for a, b in zip(subtable[0], subtable[1:]))
        if memo[col]:
            sorted_cols.add(i)
    if len(sorted_cols) > 0:
        return True
    return False

def solve():
    ans = "No"
    for col in range(m):
        sorted_in_col = True
        prev_max = rows[0][col]
        for i in range(1, n):
            if rows[i][col] < prev_max:
                sorted_in_col = False
                break
            prev_max = rows[i][col]
        if not sorted_in_col:
            continue
        for l, r in range(k):
            subtable = [row[col] for row in rows[l:r+1]]
            if check_sorted(subtable):
                ans = "Yes"
                return
    print(ans)

if __name__ == "__main__":
    solve()
