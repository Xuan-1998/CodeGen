if __name__ == "__main__":
    n_max = int(input())
    k_perms = int(input())
    output = count_prime_perms(n_max, k_perms)
    print(*output)
