import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

dp = [[0] * (m + 1) for _ in range(n + 1)]

pq = [(arr[0], 1)]  # priority queue with the first element and its beauty value
for i in range(2, n + 1):
    if arr[i] % bad_primes[0] == 0:
        good_prime = True
    else:
        good_prime = False

    for j in range(i - 1, -1, -1):  # fill dp from right to left
        if good_prime and pq[0][0] < arr[j]:
            heapq.heappop(pq)
        if not good_prime or pq[0][0] < arr[j]:
            heapq.heppush(pq, (arr[i], i))

    for j in range(m + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i - 1].index(max(dp[i - 1])) + 1)

print(max(dp[n]))
