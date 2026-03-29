import sys

def solve():
    n, q = map(int, input().split())
    signs = list(input())
    cumulative_sum = [0] * (n + 1)
    for i in range(n):
        cumulative_sum[i+1] = cumulative_sum[i] + (1 if signs[i] == '+' else -1)

    results = []
    for _ in range(q):
        l, r = map(int, input().split())
        start_cumulative_sum = cumulative_sum[l-1]
        end_cumulative_sum = cumulative_sum[r]
        min_diff = float('inf')
        for i in range(l-1, r):
            cumulative_sum_start = cumulative_sum[i]
            cumulative_sum_end = cumulative_sum[r]
            diff = abs(cumulative_sum_end - cumulative_sum_start)
            if diff < min_diff:
                min_diff = diff
        results.append(min_diff)

    print(*results, sep='\n')

if __name__ == '__main__':
    solve()
