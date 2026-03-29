import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_permutations(n):
    permutations = set()
    def permute(nums):
        if len(nums) == 1:
            permutations.add(int("".join(map(str, nums))))
        else:
            for i in range(len(nums)):
                remaining = nums[:i] + nums[i+1:]
                permute(remaining)
                if int("".join(map(str, nums))) > 0:
                    permutations.add(int("".join(map(str, nums))))
    permute(list(str(n)))
    return len(permutations)

def solve():
    n_max, k_perms = map(int, sys.stdin.readline().split())
    prime_count = 0
    smallest_prime = None
    largest_prime = None

    for i in range(2, n_max):
        if is_prime(i) and count_permutations(i) == k_perms:
            prime_count += 1
            if smallest_prime is None or i < smallest_prime:
                smallest_prime = i
            if largest_prime is None or i > largest_prime:
                largest_prime = i

    print([prime_count, smallest_prime, largest_prime])

if __name__ == "__main__":
    solve()
