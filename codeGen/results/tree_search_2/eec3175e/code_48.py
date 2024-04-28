def memoized_is_divisible(arr):
    memo = {0: True}  # Base case: sum of 0 is always divisible

    for num in arr:
        new_memo = {}
        for k, v in memo.items():
            new_memo[k + num] = new_memo.get(k + num, v) and v
            new_memo[k] = new_memo.get(k, v)
        memo.update(new_memo)

    return memo

def find_subset_sum_divisible_by_m(arr, m):
    memo = memoized_is_divisible(arr)

    for i in range(1, len(arr) + 1):  # Try all possible subset sizes
        for j in range(i):  # Check all possible subsets of size j
            if (memo.get(sum(arr[:j]), False)) and (sum(arr[j:]) % m == 0):
                return True

    return False

n, m = map(int, input().split())  # Read n, m from stdin
arr = list(map(int, input().split()))  # Read the array of integers from stdin

print(find_subset_sum_divisible_by_m(arr, m))  # Print the result to stdout
