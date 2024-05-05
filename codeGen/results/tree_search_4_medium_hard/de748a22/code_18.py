def solve():
    n, q = map(int, input().split())
    signs = list(input())

    # Initialize DP table
    dp = {(0, i): 0 for i in range(n)}
    for i in range(1, n):
        dp[(i, i)] = 1 if signs[i-1] == '-' else -1

    for _ in range(q):
        l, r = map(int, input().split())
        total_sum = sum(signs[l:r+1])
        prefix_sum = sum(signs[:l]) if l > 0 else 0
        suffix_sum = sum(signs[r:]) if r < n-1 else 0

        remaining_sum = total_sum - prefix_sum - suffix_sum
        removed_count = dp.get((0, r), 0) - dp.get((l, r), 0)

        if remaining_sum == 0:
            print(removed_count)
        else:
            # Find the minimal number of elements that need to be removed
            for i in range(min(l, r), max(l, r)):
                if signs[i] != (remaining_sum > 0):
                    removed_count += 1
                    remaining_sum -= 2

            print(removed_count)

if __name__ == '__main__':
    solve()
