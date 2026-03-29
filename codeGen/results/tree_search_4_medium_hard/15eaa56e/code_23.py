import sys

def solve():
    n, m = map(int, input().split())
    table = []
    for _ in range(n):
        row = list(map(int, input().split()))
        table.append(row)

    k = int(input())
    tasks = []
    for _ in range(k):
        l, r = map(int, input().split())
        tasks.append((l-1, r))

    def is_sorted(column):
        return all(table[i][column] <= table[i+1][column] for i in range(n-1))

    result = "Yes"
    for task in tasks:
        row_start, row_end = task
        if not all(is_sorted(column) for column in range(m)):
            result = "No"
            break

    print(result)

if __name__ == "__main__":
    solve()
