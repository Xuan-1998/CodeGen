from sys import stdin, stdout

def solve():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        arr = list(map(int, stdin.readline().split()))
        left_sum = sum(arr[:n//2])
        max_partitions = 0
        for i in range(n-1, -1, -1):
            if sum(arr[:i]) == left_sum:
                max_partitions = max(max_partitions, i // n)
        stdout.write(str(max_partitions) + '\n')

solve()
