def count_blocks(n):
    MOD = 998244353

    # Initialize a dictionary to store the memoization results
    memo = {}

    def helper(k):
        if k in memo:
            return memo[k]

        if k == 0:
            result = 1
        elif k % 2 == 0 and k // 2 in memo:
            result = (memo[k // 2] + memo[k // 2]) % MOD
        else:
            count = 0
            for i in range(10 ** n, 10 ** (n - k), -1):
                if str(i).zfill(n)[-k:] == str(i).zfill(n)[:k]:
                    count += 1
            result = count

        memo[k] = result
        return result

    total_count = [0] * (n + 1)
    for i in range(1, n + 1):
        total_count[i] = helper(i)

    print(*total_count[1:], sep=' ')

# Read the input and call the function
n = int(input())
count_blocks(n)
