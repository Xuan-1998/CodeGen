from sys import stdin

def can_reach_last_index(arr):
    n = len(arr)
    dp = [False] * n
    max_reachable = 0
    
    for i in range(n):
        if i <= max_reachable:
            dp[i] = any(j + arr[j] >= i for j in range(max_reachable+1))
            if not dp[i]:
                max_reachable = i - 1
            else:
                max_reachable = i
        else:
            return False
    
    return dp[-1]

if __name__ == "__main__":
    arr = list(map(int, stdin.readline().split()))
    print(can_reach_last_index(arr))
