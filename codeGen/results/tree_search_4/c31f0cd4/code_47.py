from collections import defaultdict

def distinct_sums(arr):
    N, sum = len(arr), sum(arr)
    memo = [[defaultdict(int) for _ in range(sum+1)] for _ in range(N+1)]

    for i in range(N+1):
        for s in range(sum+1):
            if i == 0 and s == 0:
                memo[i][s] = [0]
            elif i > 0:
                if s >= arr[i-1]:
                    for prev_sum in memo[i-1][s-arr[i-1]]:
                        memo[i][s][prev_sum+arr[i-1]] += 1
                if s >= 0:
                    memo[i][s].update(memo[i-1][s])

    distinct_sums = list(set([sum for i, sums in enumerate(memo[N]) for sum in sums]))
    return ' '.join(map(str, sorted(distinct_sums)))

# Example usage:
arr = [1, 2, 3]
print(distinct_sums(arr))  # Output: "0 1 2 3 4"
