def simulate_sequence(n, sequence):
    dp = {(0, 0): 0}
    for x in range(1, n + 1):
        y = 0
        cycle_length = 1
        while (x, y) not in dp and x <= n:
            dp[(x, y)] = cycle_length
            x += sequence[x]
            y += sequence[x]
            cycle_length += 1
    return [dp.get((i + 1, 0), -1) for i in range(n - 1)]

def main():
    n = int(input())
    sequence = list(map(int, input().split()))
    print(*simulate_sequence(n, sequence))

if __name__ == "__main__":
    main()
