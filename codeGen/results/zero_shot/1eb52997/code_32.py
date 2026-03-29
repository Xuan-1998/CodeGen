def count_mirror_options(grid):
    east_side = [row[-1] for row in grid]
    options = 0
    for i in range(len(east_side)):
        if east_side[i] == '.':
            is_blocked = False
            for j in range(i, len(east_side)):
                if east_side[j] == '#':
                    is_blocked = True
                    break
            if not is_blocked:
                options += 1
    return options

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        grid = [list(input().strip()) for _ in range(N)]
        print(count_mirror_options(grid))

if __name__ == "__main__":
    main()
