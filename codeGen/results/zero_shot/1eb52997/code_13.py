import sys

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        count = 0
        for _ in range(N):
            row = sys.stdin.readline().strip()
            cells = list(row)
            for i, cell in enumerate(cells):
                if cell == '.':
                    # Check cells to the right and above
                    has_rock = False
                    for j in range(i+1, N):
                        if cells[j] == '#':
                            has_rock = True
                            break
                    if not has_rock:
                        count += 1
        print(count)

if __name__ == "__main__":
    main()
