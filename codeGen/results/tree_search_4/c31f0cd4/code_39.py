from collections import defaultdict

def find_distinct_sums():
    N = int(input())
    arr = list(map(int, input().split()))
    distinct_sums = set()

    # Initialize dp dictionary with default value 0
    dp = defaultdict(int)

    for i in range(N):
        for sum_val in range(arr[i], 2*arr[i]+1):  # Change the range according to your requirement
            if not dp[sum_val]:
                dp[sum_val] = 1
                distinct_sums.add(sum_val)
            for k in range(arr[i]):
                if dp.get(k):
                    dp[sum_val-k] += 1

    print(' '.join(map(str, sorted(distinct_sums))))

if __name__ == "__main__":
    find_distinct_sums()
