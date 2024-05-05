from collections import defaultdict

def solve():
    n_max, k_perms = map(int, input().split())
    dp = defaultdict(int)
    count = 0
    smallest = largest = 0

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def count_perms(n):
        perms = set()
        for p in permutations(str(n)):
            num = int(''.join(p))
            perms.add(num)
        return len([p for p in perms if is_prime(p)])

    def dfs(n, k):
        nonlocal count, smallest, largest
        if n > n_max:
            return
        if not is_prime(n):
            return
        perms = count_perms(n)
        dp[perms] += 1
        if perms == k_perms:
            count += 1
            smallest = min(smallest, n)
            largest = max(largest, n)
        dfs(n + 1, k)

    dfs(2, k_perms)
    return [count, smallest, largest]

print(solve())
