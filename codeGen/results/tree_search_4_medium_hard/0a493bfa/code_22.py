==BEGIN SOLUTION==
def max_beauty(arr, bad_primes):
    n = len(arr)
    table = [[0] * (n + 1) for _ in range(m + 1)]

    def helper(start, end, is_odd):
        if start > end:
            return 0
        mid = (start + end) // 2
        if is_odd:
            if arr[mid] in bad_primes:
                left = helper(start, mid - 1, False)
                right = helper(mid + 1, end, True)
                return max(left, right)
            else:
                left = helper(start, mid - 1, not (arr[mid] % 2))
                right = helper(mid + 1, end, is_odd and arr[mid] % 2 != 0)
                return max(left, right) if is_odd and arr[mid] in bad_primes else min(left, right)
        else:
            left = helper(start, mid - 1, False)
            right = helper(mid + 1, end, True)
            return max(left, right)

    return helper(0, n - 1, False)


# Read inputs
n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(max_beauty(arr, bad_primes))
