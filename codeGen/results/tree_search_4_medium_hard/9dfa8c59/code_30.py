from collections import defaultdict

def count_prime_permutations():
    n_max, k_perms = map(int, input().split())
    prime_numbers = set()
    permutation_counts = defaultdict(int)

    for num in range(2, n_max):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.add(str(num))
            permutation_count = len(set(map(lambda x: ''.join(sorted(str(x))), prime_numbers)))
            permutation_counts[permutation_count] += 1

    sorted_permutation_counts = sorted(permutation_counts.items(), reverse=True)
    count, smallest, largest = 0, float('inf'), -float('inf')

    for _, count in sorted_permutation_counts:
        if count == k_perms:
            for num in prime_numbers:
                if str(num) in permutation_counts[count]:
                    count += permutation_counts[count]
                    if len(str(num)) < smallest:
                        smallest = len(str(num))
                    if len(str(num)) > largest:
                        largest = len(str(num))
                    break
        else:
            break

    return [count, smallest, largest]

print(count_prime_permutations())
