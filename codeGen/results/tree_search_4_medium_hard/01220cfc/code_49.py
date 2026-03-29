def canReach(arr):
    dp = [False] * len(arr)

    def helper(i):
        if i >= len(arr) or dp[i]:
            return True

        if not dp[i]:
            for j in range(1, i + 2):
                if j <= i and arr[j - 1] >= i - j:
                    dp[i] = True
                    break
        return dp[i]

    return helper(len(arr) - 1)

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print("Yes" if canReach(arr) else "No")

if __name__ == "__main__":
    main()
