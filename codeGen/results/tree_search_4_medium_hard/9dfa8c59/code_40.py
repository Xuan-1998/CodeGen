if __name__ == '__main__':
    n_max, k_perms = map(int, input().split())
    result = find_prime_permutations(n_max, k_perms)
    print(result[0], result[1], result[2])
