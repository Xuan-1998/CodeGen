def beauty(array):
    memo = {0: 0}  # Base case: an empty array has a beauty of 0

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def max_beauty(i):
        if i in memo:
            return memo[i]

        beauty_i = array[i]
        for j in range(len(array)):
            if j != i:
                common_divisor = gcd(array[j], array[i])
                if common_divisor not in bad_primes:
                    beauty_j = max_beauty(j)
                    beauty_i += beauty_j
        return memo[i] = beauty_i

    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))

    max_beauty_value = 0
    for i in range(n):
        if array[i] not in bad_primes:
            beauty_value = max_beauty(i)
            max_beauty_value = max(max_beauty_value, beauty_value)

    print(max_beauty_value)
