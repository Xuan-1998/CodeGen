from collections import defaultdict

def find_longest_increasing_subsequences(arr):
    n = len(arr)
    dp = [1] * n
    memo = defaultdict(int)

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    max_length = max(dp)
    count = sum(1 for x in dp if x == max_length)

    return count

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    
    print(find_longest_increasing_subsequences(arr))

if __name__ == "__main__":
    main()
