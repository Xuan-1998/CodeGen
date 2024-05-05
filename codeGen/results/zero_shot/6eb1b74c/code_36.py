import sys

def solve():
    # Read input from stdin
    t = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    strings = [sys.stdin.readline().strip() for _ in range(n)]

    # Initialize variables
    m = 0
    used_strings = []

    # Iterate through the text, checking for occurrences of each string
    i = 0
    while i < len(t):
        found = False
        for s in strings:
            j = t.find(s, i)
            if j != -1:
                found = True
                break
        if not found:
            i += 1
            continue

        # If this is a new substring that needs to be colored
        m += 1
        used_strings.append((strings.index(s), i))

        # Update the starting position for the next iteration
        i = j + len(s)

    # Output the minimum number of steps and the chosen strings
    print(m)
    for w, p in used_strings:
        print(f"{w} {p}")

if __name__ == "__main__":
    solve()
