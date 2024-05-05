while True:
    try:
        n_max, k_perms = map(int, input().split())
        break
    except ValueError:
        pass

count = 0
smallest = float('inf')
largest = 0

for i in range(2, n_max):
    if is_prime(i):
        perms = get_permutations(i)
        if len(perms) == k_perms:
            count += 1
            smallest = min(smallest, i)
            largest = max(largest, i)

print([count, smallest, largest])
