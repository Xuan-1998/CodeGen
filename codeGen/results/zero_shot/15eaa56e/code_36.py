import sys

def is_subtable_sorted(table, l, r):
    for j in range(len(table[0])):
        col = [row[j] for row in table[l-1:r]]
        if not all(col[i] <= col[i+1] for i in range(len(col)-1)):
            return False
    return True

def main():
    n, m = map(int, sys.stdin.readline().split())
    table = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
    k = int(sys.stdin.readline())
    tasks = []
    for _ in range(k):
        l, r = map(int, sys.stdin.readline().split())
        tasks.append((l, r))

    for task in tasks:
        if is_subtable_sorted(table, *task):
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()
