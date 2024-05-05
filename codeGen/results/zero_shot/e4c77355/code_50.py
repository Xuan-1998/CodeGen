def read_input():
    return [int(x) for x in input().split()]

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [[1] * n for _ in range(n)]
    
    max_length = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                dp[i][j] = min((dp[k][i-1] + 1) for k in range(i)) + 1
                max_length = max(max_length, dp[i][j])
    
    return max_length

def main():
    arr = read_input()
    print(longest_increasing_subsequence(arr))

if __name__ == "__main__":
    main()
