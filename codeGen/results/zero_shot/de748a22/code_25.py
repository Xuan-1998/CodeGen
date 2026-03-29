import sys

def solve():
    n, q = map(int, input().split())
    signs = list(input())

    # Calculate prefix sum array
    prefix_sum = [0]
    for sign in signs:
        prefix_sum.append(prefix_sum[-1] + (1 if sign == '+' else -1))

    result = []
    for _ in range(q):
        l, r = map(int, input().split())
        diff = prefix_sum[r] - prefix_sum[l-1]
        result.append(min(r-l+1, abs(diff)))

    print(*result, sep='\n')

if __name__ == '__main__':
    solve()
