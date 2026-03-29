import math

def count_permutations(n):
    total_permutations = math.factorial(2 * n + 1)
    favorable_permutations = 0
    for _ in range(math.factorial(n)):
        towns_to_towers = [0] * (n + 1)
        for i in range(1, n + 1):
            town_index = random.randint(1, n)
            if towns_to_towers[town_index] == 0:
                towns_to_towers[town_index] += 1
            else:
                break
        if sum(towns_to_towers) == n and towns_to_towers[0] == 0 and towns_to_towers[n + 1] == 0:
            favorable_permutations += 1
    return (favorable_permutations * math.factorial(2 * n + 1)) % 998244353

n = int(input())
print(count_permutations(n))
