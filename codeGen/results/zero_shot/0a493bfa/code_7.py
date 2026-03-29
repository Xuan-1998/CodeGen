n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
bad_primes = set(map(int, sys.stdin.readline().split()))

print(optimize_algorithm(a))
