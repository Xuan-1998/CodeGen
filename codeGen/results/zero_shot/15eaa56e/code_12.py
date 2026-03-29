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
        tasks.append((l, r))

    result = "No"
    for task in tasks:
        l, r = task
        for col in range(m):
            subtable = [row[col] for row in table[l-1:r]]
            if is_sorted(subtable):
                result = "Yes"
                break

    print(result)

def is_sorted(lst):
    return all(x <= y for x, y in zip(lst, lst[1:]))

if __name__ == "__main__":
    solve()
