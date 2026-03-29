import heapq

def max_beauty(n, m, bad_primes):
    # Initialize the array with the given values
    arr = list(map(int, input().split()))

    # Compute the beauty of each element in the array
    beauty = [0] * (n + 1)
    for i in range(1, n + 1):
        gcd = arr[i - 1]
        for j in range(i, 0, -1):
            gcd = abs(gcd // arr[j - 1])
            if gcd == 1:
                break
            beauty[i] += (arr[i - 1] // gcd) * (i > 1)
            gcd = min(gcd, bad_primes[0]) if any(p <= gcd for p in bad_primes) else gcd

    # Compute the maximum beauty of the array using dynamic programming
    dp = [0] * (n + 1)
    pq = [(arr[0], 0)]
    while pq:
        val, idx = heapq.heappop(pq)
        if idx < n:
            for j in range(idx + 1, n + 1):
                gcd = abs(val // arr[j - 1])
                if gcd == 1:
                    break
                dp[j] = max(dp[j], dp[idx] + (arr[j - 1] // gcd) * (j > idx))
                gcd = min(gcd, bad_primes[0]) if any(p <= gcd for p in bad_primes) else gcd
                heapq.heappush(pq, (-dp[j], j))

    return dp[n]

n, m = map(int, input().split())
bad_primes = list(map(int, input().split()))
print(max_beauty(n, m, bad_primes))
