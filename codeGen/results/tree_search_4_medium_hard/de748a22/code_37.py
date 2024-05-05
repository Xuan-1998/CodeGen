def solve():
    n, q = map(int, input().split())
    arr = list(input())

    # Calculate the initial sign_sum and memoize it
    sign_sum = sum(1 if c == '+' else -1 for c in arr)
    memo = {sign_sum: (0, n)}

    # Process each query
    for _ in range(q):
        l, r = map(int, input().split())
        left, right = memo[binary_search(sign_sum)]

        # Calculate the number of elements that can be removed from this query range
        if left == 0:
            res = r - l + 1 - (right - left)
        else:
            res = r - l

        print(res)

def binary_search(target_sign_sum):
    low, high = min(memo), max(memo)
    while high - low > 1:
        mid = (low + high) // 2
        if memo[mid] < target_sign_sum:
            low = mid
        else:
            high = mid
    return memo[high]

if __name__ == "__main__":
    solve()
