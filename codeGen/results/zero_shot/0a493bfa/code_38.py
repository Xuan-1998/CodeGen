def max_beaauty(n, m, a):
    # TO DO: Implement the main logic using recursion or dynamic programming
    pass

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bad_primes = set(map(int, input().split()))
    print(max_beaauty(n, m, a))
