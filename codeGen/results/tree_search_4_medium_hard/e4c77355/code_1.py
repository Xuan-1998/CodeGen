from typing import List

def longest_increasing_subsequence(arr: List[int]) -> int:
    memo = {}

    def lis(i: int) -> int:
        if i not in memo:
            max_len = 1
            for j in range(i):
                if arr[j] < arr[i]:
                    max_len = max(max_len, 1 + lis(j))
            memo[i] = max_len
        return memo[i]

    return max(lis(i) for i in range(len(arr)))

if __name__ == "__main__":
    import sys
    arr = [int(x) for x in sys.stdin.readline().split()]
    print(longest_increasing_subsequence(arr))
