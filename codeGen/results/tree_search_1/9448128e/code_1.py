MOD = 998244353

def main():
    N = int(input())
    dp = {}
    total = 0

    for _ in range(N):
        A = list(map(int, input().split()))[1:]
        new_dp = {}
        new_total = 0

        for x in A:
            # Calculate the number of sequences ending with x, which is the total
            # from the previous set minus the number of sequences that ended with x
            # in the previous set (if any), to ensure no two adjacent elements are equal.
            new_dp[x] = (total - dp.get(x, 0)) % MOD
            new_total = (new_total + new_dp[x]) % MOD

        dp = new_dp
        total = new_total

    # The answer is the sum of all dp values after processing the last set.
    print(total)

if __name__ == "__main__":
    main()
