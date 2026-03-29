import sys

def solve(n, m, k, table):
    # Initialize the state expression dictionary
    state = {i: True for i in range(m)}

    # Iterate through each task (l, r)
    for l, r in [list(map(int, line.split())) for line in sys.stdin.read().splitlines()]:
        unsorted_cols = set()

        # Iterate through columns from left to right
        for i in range(m):
            if state[i] and all(table[j][i] == table[l-1][i] for j in range(l, r+1)):
                unsorted_cols.add(i)

        # If no columns are unsorted, return "Yes"
        if not unsorted_cols:
            print("Yes")
            sys.exit()

    # If we reach this point, it means all tasks failed to find a sorted column
    print("No")

if __name__ == "__main__":
    n, m = map(int, input().split())
    table = [list(map(int, line.split())) for line in [input() for _ in range(n)]]
    k = int(input())
    solve(n, m, k, table)
