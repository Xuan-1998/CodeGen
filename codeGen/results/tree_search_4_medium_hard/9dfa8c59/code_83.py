import sys

def count_prime_permutations(n, k):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_permutations(num):
        num_str = str(num)
        permutations = set()
        for p in range(len(num_str)):
            for q in range(p+1, len(num_str)+1):
                permutation = int(''.join(sorted(num_str[p:q])))
                if permutation not in permutations:
                    permutations.add(permutation)
        return len(permutations)

    prime_counts = {}
    for num in range(2, n + 1):
        if is_prime(num):
            count = get_permutations(num)
            if count in prime_counts:
                prime_counts[count].add(num)
            else:
                prime_counts[count] = {num}

    answer = [0, float('inf'), -float('inf')]
    for count, primes in prime_counts.items():
        if count == k:
            answer[0] += len(primes)
            answer[1] = min(answer[1], min(primes))
            answer[2] = max(answer[2], max(primes))

    print(*answer)

# Read input from stdin
n_max, k_perms = map(int, sys.stdin.readline().split())

count_prime_permutations(n_max, k_perms)
