import sys

def solve():
    n, q = map(int, sys.stdin.readline().split())
    signs = list(map(lambda x: +1 if x == '+' else -1, sys.stdin.readline()))
    prefix_sum = [0]
    suffix_sum = [0]

    for sign in signs:
        prefix_sum.append(prefix_sum[-1] + sign)
        suffix_sum.append(suffix_sum[-1] + sign)

    results = []
    for _ in range(q):
        l, r = map(int, sys.stdin.readline().split())
        query_range_prefix_sum = prefix_sum[r] - prefix_sum[l-1]
        query_range_suffix_sum = suffix_sum[n-1] - suffix_sum[r]

        if query_range_prefix_sum == 0 and query_range_suffix_sum == 0:
            results.append(0)
        else:
            removed_elements = abs(query_range_prefix_sum) + abs(query_range_suffix_sum)
            results.append(removed_elements)

    for result in results:
        print(result, file=sys.stdout)

if __name__ == "__main__":
    solve()
