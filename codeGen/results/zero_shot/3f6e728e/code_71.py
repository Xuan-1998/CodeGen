def solve():
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))

        # Sort the radii of the upper and lower hemispheres
        U.sort()
        L.sort()

        # Initialize a dictionary to store the number of X-sequences for each length
        dp = [0] * (C + 1)
        dp[0] = 1

        # Calculate the number of X-sequences for each length
        for i in range(1, C + 1):
            if U:
                j = binary_search(U, i)
                dp[i] += sum(dp[:j])
            if L:
                k = binary_search(L, i)
                dp[i] += sum(dp[:k])

        # Print the output
        print(*dp, sep=' ')

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            high = mid - 1
        else:
            low = mid + 1
    return low

if __name__ == '__main__':
    solve()
