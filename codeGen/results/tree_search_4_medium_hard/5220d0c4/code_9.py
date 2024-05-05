def find_max_beauty():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = set(map(int, input().split()))

    dp = {}
    for i in range(n):
        min_prime = next((p for p in range(2, arr[i] + 1) if arr[i] % p == 0 and p not in bad_primes), arr[i])
        if min_prime in dp:
            dp[min_prime].append(arr[i])
        else:
            dp[min_prime] = [arr[i]]

    max_beauty = 0
    for prime, good_primes in dp.items():
        beauty = len(good_primes)
        if beauty > max_beauty:
            max_beauty = beauty

    return max_beauty

print(find_max_beauty())
