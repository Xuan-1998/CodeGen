def count_good_subsequences(n, a):
    MOD = 10**9 + 7
    good_subseqs = 0

    # Handle edge case where n == 1 (only one element in the array)
    if n == 1:
        return 1

    # Iterate over all possible subsequences of length 2 to n-1
    for subseq_len in range(2, n):
        for i in range(n - subseq_len + 1):
            subseq = [a[j] for j in range(i, i + subseq_len)]
            prime_factors = [2]
            prev_prime_factor = 2

            # Check if all elements in the subsequence have consecutive prime factors
            for num in subseq:
                prime_factors.append(find_next_prime_factor(num, prev_prime_factor))
                prev_prime_factor = prime_factors[-1]

            # If the subsequence has consecutive prime factors, it's good
            if len(set(prime_factors)) == len(prime_factors):
                good_subseqs += 1

    return good_subseqs % MOD


def find_next_prime_factor(num, prev_prime_factor):
    for i in range(prev_prime_factor + 1, int(num ** 0.5) + 1):
        if is_prime(i):
            return i
    return num


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Read input from stdin and call the function to count good subsequences
n = int(input())
a = list(map(int, input().split()))
print(count_good_subsequences(n, a))
