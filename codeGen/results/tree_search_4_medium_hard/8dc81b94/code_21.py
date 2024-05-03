import sys

def can_zero_out(arr):
    n = len(arr)
    memo = {}

    def dp(i, sum_val, max_val, min_val):
        if (i, sum_val, max_val, min_val) in memo:
            return memo[(i, sum_val, max_val, min_val)]

        if i == n:
            return "YES" if sum_val == 0 else "NO"

        # Decrement from the beginning
        dp_res = dp(i + 1, sum_val - arr[i], max(min_val, arr[i]), min(max_val, arr[i]))
        if dp_res != "NO":
            memo[(i, sum_val, max_val, min_val)] = dp_res
            return dp_res

        # Decrement from the end
        dp_res = dp(i + 1, sum_val - arr[n - i - 1], max(min_val, arr[n - i - 1]), min(max_val, arr[n - i - 1]))
        if dp_res != "NO":
            memo[(i, sum_val, max_val, min_val)] = dp_res
            return dp_res

        # If it's not possible to make the array equal to zero
        return "NO"

    return dp(0, sum(arr), max(arr), min(arr))

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(can_zero_out(arr))

if __name__ == "__main__":
    main()
