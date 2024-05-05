def count_prime_permutations(n_max, k_perms):
    dp = [[0 for _ in range(k_perms + 1)] for _ in range(n_max + 1)]
    smallest = float('inf')
    largest = -float('inf')

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def count_permutations(n, k):
        if k == 0:
            return 1
        count = 0
        for digit in str(n):
            new_n = int(''.join(sorted(digit)))
            if is_prime(new_n) and dp[new_n][k - 1]:
                count += 1
        return count

    for n in range(2, n_max + 1):
        if is_prime(n):
            count = count_permutations(n, k_perms)
            if count:
                smallest = min(smallest, n)
                largest = max(largest, n)
                dp[n][k_perms] += 1

    return [dp[n_max][k_perms], smallest, largest]
