def process_query(prefix_sum, suffix_sum, l, r):
    # Calculate the sign-variable sum for the query range
    left_sum = prefix_sum[r] - (l > 0) * prefix_sum[l - 1]
    right_sum = suffix_sum[r + 1] - (n - r - 1 > 0) * suffix_sum[n - l]

    # Find the minimal number of elements that need to be removed
    if left_sum == 0:
        return r - l + 1
    elif right_sum == 0:
        return n - r - 1
    else:
        if left_sum > 0:
            return min(r - l + 1, n - r - 1)
        else:
            return min(r - l + 1, r - l)

n, q = map(int, input().split())
signs = list(input())

prefix_sum, suffix_sum = preprocess_array(signs)

for _ in range(q):
    l, r = map(int, input().split())
    print(process_query(prefix_sum, suffix_sum, l, r))
