import sys

def check_sorted_table(n, m, tasks):
    # Initialize the state expression
    state = {i: True for i in range(m)}

    for row in range(n):
        for col in range(m):
            if not state[col]:
                break
            for _ in range(row+1):
                sys.stdin.readline()
            current_row = [int(x) for x in sys.stdin.readline().split()]
            state[col] = all(current_row[i] <= current_row[i+1] for i in range(len(current_row)-1))

    # Check the tasks
    for task in tasks:
        l, r = map(int, task.split())
        for col in range(m):
            if not state[col]:
                break
            subtable = [row[col] for row in range(l-1, r)]
            if not all(subtable[i] <= subtable[i+1] for i in range(len(subtable)-1)):
                return "No"

    return "Yes"


# Read the input
n, m = map(int, sys.stdin.readline().split())
tasks = []
for _ in range(int(sys.stdin.readline())):
    tasks.append(list(map(int, sys.stdin.readline().split())))

print(check_sorted_table(n, m, tasks))
