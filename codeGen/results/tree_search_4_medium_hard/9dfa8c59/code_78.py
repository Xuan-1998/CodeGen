def count_prime_permutations(n_max, k_perms):
    prime_info = {"count": 0, "smallest": float('inf')}

    def is_prime(n):
        memo = {}
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
            memo[i] = True
        return True

    for num in range(2, n_max + 1):
        if is_prime(num):
            permutations = []
            for digit in str(num):
                if int(digit) not in permutations:
                    permutations.append(int(digit))
            if len(permutations) == k_perms:
                prime_info["count"] += 1
                prime_info["smallest"] = min(prime_info["smallest"], num)

    return [prime_info["count"], prime_info["smallest"], n_max]
