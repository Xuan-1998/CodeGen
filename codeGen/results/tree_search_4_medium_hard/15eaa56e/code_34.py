def is_sorted_table(table):
    n, m = len(table), len(table[0])
    max_values = [[0] * (m + 1) for _ in range(n + 1)]

    def is_sorted_subtable(l, r):
        for col in range(m):
            max_val = max_values[l][col]
            for row in range(l, r + 1):
                if table[row][col] > max_val:
                    return False
                max_values[row][col + 1] = table[row][col]
            return True

    tasks = [list(map(int, input().split())) for _ in range(int(input()))]

    for task in tasks:
        l, r = task
        if is_sorted_subtable(l - 1, r):
            print("Yes")
            return

    print("No")

if __name__ == "__main__":
    table = [list(map(int, input().split())) for _ in range(int(input()))]
    is_sorted_table(table)
