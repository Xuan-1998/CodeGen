def get_permutations(n):
    """Get the number of unique permutations for a given number n."""
    if str(n) == "".join(sorted(str(n))):
        return 1
    return len(set(map(int, "".join(sorted(str(n))))))

def main():
    n_max, k_perms = map(int, input().split())
    count = 0
    smallest = largest = float('inf')
    dp = {}

    # Iterate through all prime numbers up to n_max:
    for p in range(2, n_max + 1):
        if p not in dp:
            is_prime = True
            for i in range(2, int(p ** 0.5) + 1):
                if p % i == 0:
                    is_prime = False
                    break
            if is_prime:
                k_perms_count = get_permutations(p)
                dp[p] = (p, k_perms_count)

    # Count the number of prime numbers with k_perms permutations and find the smallest and largest:
    for (p, k_perms_count) in dp.values():
        if k_perms_count == k_perms:
            count += 1
            smallest = min(smallest, p)
            largest = max(largest, p)

    print([count, smallest, largest])

if __name__ == "__main__":
    main()
