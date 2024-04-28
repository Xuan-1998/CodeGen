def count_good_sequences(n, k):
    s = [0] * (n + 1)
    for i in range(2, n + 1):
        for j in range(i):
            if j % i == 0:
                s[i] += 1

    dp = [0] * (n + 1)
    for i in range(1, n):
        for j in range(1, i // gcd(j, i) + 1):
            if i % (j + 1) == 0 and k > 1:
                dp[i] += s[j]
    return (dp[n] * 2 - sum(s)) % (10**9 + 7)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(count_good_sequences(n, k))
