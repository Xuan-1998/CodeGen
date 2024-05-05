def solve():
    n, m, k = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(n)]
    tasks = []
    for _ in range(k):
        l, r = map(int, input().split())
        tasks.append((l, r))

    dp = {"No": True}  # default value

    def check_sorted(col, rows):
        max_val = float('-inf')
        for row in rows:
            if row[col-1] > max_val:
                max_val = row[col-1]
        return [row for row in rows if all(row[i] <= row[i+1] for i in range(len(rows[0])-1))]

    for l, r in tasks:
        dp[l] = "No"
        for col in range(m):
            rows = [table[row][col:] for row in range(l-1, r)]
            if sorted_rows := check_sorted(col, rows):
                for i, row in enumerate(sorted_rows):
                    dp[l+i] = "Yes" if not all(dp[j] == "No" for j in range(l, l+i+1)) else "No"

    print("Yes" if any(val == "Yes" for val in dp.values()) else "No")

solve()
