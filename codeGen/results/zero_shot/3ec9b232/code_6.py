def solve():
    n = int(input())  # read the size of array M
    m = list(map(int, input().split()))  # read the elements of array M
    
    MOD = 10**9 + 7
    
    dp = [0] * (n + 1)  # dynamic programming table
    dp[0] = 1  # base case: there is one way to create an empty collection
    
    for i in range(n):
        dp[i + 1] = dp[i]  # if the current element is not included, we have the same number of ways as before
        if m[i] > 0:
            for j in range(m[i], n):
                if m[j] == m[i]:  # if there are duplicates
                    break
                dp[i + 1] = (dp[i + 1] + dp[j]) % MOD  # add the number of ways to create a collection ending at this element
    
    print(dp[n])  # print the answer

if __name__ == "__main__":
    solve()
