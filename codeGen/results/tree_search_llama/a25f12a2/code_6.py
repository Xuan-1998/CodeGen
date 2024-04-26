def find_creatures():
    heads, tails = map(int, input().split())
    total = heads + tails

    for orthus in range(2, (total + 1) // 2):
        hydra = total - orthus
        if abs(orthus - hydra) >= 2:
            return [orthus, hydra]

    return "No solutions"

print(find_creatures())
