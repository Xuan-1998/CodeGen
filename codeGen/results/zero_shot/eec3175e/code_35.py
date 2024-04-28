n, m = map(int, input().split())
numbers = list(map(int, input().split()))

print(1 if any(sum(subset) % m == 0 for r in range(len(numbers)+1) for subset in itertoolschain(*[iter(numbers)]*r)) else 0)
