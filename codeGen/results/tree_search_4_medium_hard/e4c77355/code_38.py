import sys

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [[0, []] for _ in range(n)]
    
    for i in range(n):
        max_length = 1
        subsequence = [arr[i]]
        
        for j in range(i):
            if arr[i] > arr[j]:
                prev_length, prev_subsequence = dp[j]
                if prev_length + 1 > max_length:
                    max_length = prev_length + 1
                    subsequence = prev_subsequence + [arr[i]]
                
        dp[i][0] = max_length
        dp[i][1] = subsequence
    
    return max(dp, key=lambda x: x[0])[0]

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    
    print(longest_increasing_subsequence(arr))

if __name__ == "__main__":
    main()
