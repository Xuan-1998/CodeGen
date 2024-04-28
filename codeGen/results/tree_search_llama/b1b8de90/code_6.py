import sys

def count_permutations(n):
    def recursive_sorting_permutations(k):
        if k == 0:
            return 1
        permutations = 0
        for i in range(1, k+1):
            permutations += recursive_sorting_permutations(k-1)
        return permutations

    total_permutations = 0
    for x in range(1, n+1):
        total_permutations += recursive_sorting_permutations(n-1)

    return total_permutations


n = int(sys.stdin.readline())
print(count_permutations(n))
