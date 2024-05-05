def count_prime_numbers(n_max, k_perms):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def count_permutations(num):
        digits = [int(d) for d in str(num)]
        permutations = set()
        for p in itertools.permutations(digits):
            permutation = int(''.join(map(str, p)))
            permutations.add(permutation)
        return len([p for p in permutations if is_prime(p)])

    memo = {}
    count_smallest_largest = [0, float('inf'), -float('inf')]
    for num in range(n_max, 1, -1):
        if not memo.get(num):
            prime = is_prime(num)
            perms = count_permutations(num)
            if perms == k_perms and prime:
                count_smallest_largest[0] += 1
                count_smallest_largest[1] = min(count_smallest_largest[1], num)
                count_smallest_largest[2] = max(count_smallest_largest[2], num)
            memo[num] = (prime, perms)

    return [count_smallest_largest[0], count_smallest_largest[1], count_smallest_largest[2]]

if __name__ == "__main__":
    n_max, k_perms = map(int, input().split())
    print(count_prime_numbers(n_max, k_perms))
