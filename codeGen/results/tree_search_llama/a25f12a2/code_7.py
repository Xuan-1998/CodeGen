def orthus_and_hydra(heads, tails):
    total = heads + tails
    orthus, hydra = 0, 0

    for i in range(2, min(heads, tails) // 2 + 1):
        if (heads - i) >= (tails - i):
            if (heads - i) % 2 == 0 and (tails - i) % 2 != 0:
                orthus = heads - i
                hydra = tails - i
                break

    if orthus * 2 + hydra <= total:
        return [orthus, hydra]
    else:
        return ["No solutions"]

heads, tails = map(int, input().split())
print(orthus_and_hydra(heads, tails))
