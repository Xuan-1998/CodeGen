# BEGIN SOLUTION
import sys

MOD = 10**9 + 7
def solve():
    n, k = map(int, input().split())
    dp = [0] * (n + 1)
    possible_to_increase = [False] * (n + 1)

    def dfs(i):
        if i < 0:
            return False

        if dp[i]:
            return True

        result = False
        for x in range(2**k):
            and_result = ((x >> i) & ((1 << k) - 1)) ^ (x >> k)
            xor_result = (x >> i) ^ (x >> k)
            if dfs(i + 1) and and_result >= xor_result:
                result = True
                break

        dp[i] = result
        return result

    for i in range(n):
        if not possible_to_increase[i]:
            continue
        for x in range(2**k):
            and_result = ((x >> i) & ((1 << k) - 1)) ^ (x >> k)
            xor_result = (x >> i) ^ (x >> k)
            if dfs(i + 1) and and_result >= xor_result:
                break
        possible_to_increase[i] = False

    print((dfs(0) or not any(possible_to_increase)).count(True))
# END SOLUTION
