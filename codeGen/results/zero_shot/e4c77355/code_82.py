import sys
from typing import List, Tuple

def read_input() -> List[int]:
    return [int(x) for x in sys.stdin.readline().split()]

def lis(arr: List[int]) -> int:
    n = len(arr)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

def main():
    arr = read_input()
    print(lis(arr))

if __name__ == "__main__":
    main()
