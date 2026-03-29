===BEGIN PLAN===
dp = {}
def andor(i, k):
    if i < 0:
        return [1]
    key = (i, k-1)
    if key in dp:
        return dp[key]
    and_or_greater = []
    and_or_smaller = []
    for j in andor(i-1, k-1):
        and_or_greater.append(2**k - 1) + j
        and_or_smaller.append((2**(k-1)) + 1) + j
    or_smaller = [j for j in or(i-1, k-2)]
    dp[key] = and_or_greater + and_or_smaller
    return dp[key]

def or(i, k):
    if i < 0:
        return []
    key = (i, k-1)
    if key in dp:
        return dp[key]
    result = []
    for j in range(2**k):
        if ((j >> (k-1)) & 1) == 0:  # Check if the most significant bit is not set
            result.append(j)
    dp[key] = result
    return dp[key]

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        count = 0
        and_or_results = [1]
        for i in range(n):
            a = int(input())
            if (a >> (k-1)) & 1:  # Check if the most significant bit is set
                continue
            or_result = [j for j in or(a, k-1)]
            count += len([j for j in and_or_results if all((j & x) >= x for x in or_result)])
        print(count % (10**9 + 7))

main()
