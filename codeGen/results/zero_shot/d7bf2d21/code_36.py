import sys
from collections import defaultdict

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [1] * n  # Initialize dynamic programming array with ones
    hmap = defaultdict(list)  # Hash map to store the ending indices of elements in the increasing subsequence
    
    for i in range(n):
        for j in range(i):  # Check all previous elements
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                hmap[dp[i]].append(i)  # Update hash map with the ending indices of the increasing subsequence
    
    max_length = max(dp)  # Find the length of the longest increasing subsequence
    count = 0
    
    for key in sorted(hmap):
        if key == max_length:
            count += len(hmap[key])  # Count the number of occurrences of the longest increasing subsequence
            break
    
    print(count)

if __name__ == "__main__":
    main()
