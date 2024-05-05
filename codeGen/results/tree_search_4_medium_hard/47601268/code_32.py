def doesContainConsecutiveOnes(i):
    return "1" * (i.bit_length() + 1).bit_length() != bin(i)[2:]

def count_non_consecutive Ones(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        if not doesContainConsecutiveOnes(i):
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1]

    return dp[n]

if __name__ == "__main__":
    n = int(input())
    print(count_non_consecutive Ones(n))
