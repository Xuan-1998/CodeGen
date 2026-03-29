def solve():
    n, q = map(int, input().split())
    signs = list(input())

    # Calculate prefix sum array
    prefix_sum = [0]
    sign_var_sum = 0
    for sign in signs:
        sign_var_sum += -1 if sign == '-' else 1
        prefix_sum.append(prefix_sum[-1] + sign_var_sum)

    for _ in range(q):
        l, r = map(int, input().split())
        left_sum = prefix_sum[l-1]
        right_sum = prefix_sum[r] - prefix_sum[l-1]
        min_to_remove = abs(left_sum) if left_sum < 0 else 0
        min_to_remove = min(min_to_remove, abs(right_sum))
        print(min_to_remove)

solve()
