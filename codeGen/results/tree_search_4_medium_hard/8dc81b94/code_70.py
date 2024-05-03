dp = {0: True}  # base case

def dp_func(i):
    if i in dp:
        return dp[i]
    if i == 0:  # already at the end of the array
        return True
    for j in range(1, min(i+2, len(arr))+1):  # consider all possible subarrays
        if (i-j) in dp and dp[i-j]:
            return True
    dp[i] = False  # not possible to make this sum zeroable
    return False

n = int(input())
for _ in range(n):
    n, *arr = map(int, input().split())  # read the array size and elements
    print("YES" if dp_func(sum(arr)) else "NO")  # check if it's possible to make all elements zeroable
