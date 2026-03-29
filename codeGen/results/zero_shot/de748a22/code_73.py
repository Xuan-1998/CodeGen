def solve():
    n, q = map(int, input().split())
    signs = list(map(lambda x: 1 if x == '+' else -1, input()))

    # Calculate prefix sum array
    prefix_sum = [0]
    for sign in signs:
        prefix_sum.append(prefix_sum[-1] + sign)

    for _ in range(q):
        l, r = map(int, input().split())
        left_sum = prefix_sum[l-1]
        right_sum = prefix_sum[r]

        # Calculate the minimum number of elements to remove
        min_remove = abs(left_sum - right_sum)
        print(min_remove)

if __name__ == "__main__":
    solve()
