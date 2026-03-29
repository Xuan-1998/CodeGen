import sys

def solve(n, m):
    # Calculate the initial number of digits in n
    num_digits = len(str(n))

    # Apply each operation, counting how many times a digit increases
    for _ in range(m):
        new_n = 0
        increased_count = 0
        for d in str(n):
            new_d = int(d) + 1
            if new_d > 9:  # Increased by 1, so increment the count
                increased_count += 1
            else:
                new_d = str(new_d)
            new_n = new_n * 10 + int(new_d)

        n = new_n

    # The final length is the initial length plus the number of increased digits
    return (num_digits + increased_count) % (10**9 + 7)


t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(solve(n, m))
