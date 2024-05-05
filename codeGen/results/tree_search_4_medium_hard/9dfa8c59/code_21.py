def solve():
    n_max, k_perms = map(int, input().split())
    
    primes = set()
    sieve = [True] * (n_max + 1)
    for i in range(2, int(n_max ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n_max + 1, i):
                sieve[j] = False
    for i in range(2, n_max + 1):
        if sieve[i]:
            primes.add(i)

    perm_counts = {}
    min_max_primes = [0, float('inf'), float('-inf')]

    dp = [0] * (n_max + 1)
    for num in primes:
        if len(str(num)) > k_perms:
            continue
        count = 1
        digits = sorted(str(num))
        for i in range(len(digits)):
            next_digits = ''.join([digits[j] for j in range(i) + range(i+1, len(digits))])
            next_num = int(''.join(map(str, [int(digit) for digit in next_digits])))
            if next_num > n_max:
                break
            if next_num in primes:
                count += 1
        perm_counts[num] = count
        dp[num] = count

    for i in range(2, n_max + 1):
        if dp[i] == k_perms:
            min_max_primes[0] += 1
            min_max_primes[1] = min(min_max_primes[1], i)
            min_max_primes[2] = max(min_max_primes[2], i)

    print([min_max_primes[0], min_max_primes[1], min_max_primes[2]])

if __name__ == '__main__':
    solve()
