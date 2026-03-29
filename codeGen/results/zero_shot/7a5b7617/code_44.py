import sys

def count_steady_tables():
    T = int(sys.stdin.readline().strip())
    results = []
    for _ in range(T):
        N, M = map(int, sys.stdin.readline().split())
        # Fill in the last row with non-negative integers that add up to M or less
        last_row = [i for i in range(M+1)]
        # Calculate what the sum needs to be for each subsequent row
        for i in range(N-1, 0, -1):
            target_sum = sum(last_row) + (N-i)
            last_row = [min(i, M//target_sum) for i in last_row]
        results.append(sum(1 for row in itertools.product(*[range(M+1)]*N)) % 1000000000)
    print('\n'.join(map(str, results)))
