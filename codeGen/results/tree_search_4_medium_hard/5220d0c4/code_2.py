def getMinPrimeDivisor(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return n

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def beautyDP(i, k, arr, memo):
    if (i, k) in memo:
        return memo[(i, k)]

    if i == 0:
        return 0

    minPrimeDivisor = getMinPrimeDivisor(arr[i])
    isBadPrime = isPrime(minPrimeDivisor)
    if isBadPrime and k > minPrimeDivisor:
        k = minPrimeDivisor

    beauty = beautyDP(i - 1, k, arr, memo)
    if not isBadPrime or k == minPrimeDivisor:
        beauty += arr[i]
    else:
        beauty -= arr[i]

    memo[(i, k)] = beauty
    return beauty

n, m = map(int, input().split())
arr = list(map(int, input().split()))
badPrimes = list(map(int, input().split()))

memo = {}
max_beauty = 0
for i in range(n):
    max_beauty = max(max_beauty, beautyDP(i, max(badPrimes), arr, memo))

print(max_beauty)
