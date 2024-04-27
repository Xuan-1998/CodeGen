def solve():
    total_heads, total_tails = map(int, input().split())
    orthus_heads = 0
    hydra_heads = 0

    for i in range(total_heads // 2 + 1):
        tails_left = total_tails - (total_heads - 2 * i)
        if tails_left >= 0 and tails_left % 2 == 1:
            hydra_heads = total_heads - 2 * i
            orthus_heads = 2 * i
            break

    if orthus_heads > 0 and hydra_heads > 0:
        return [orthus_heads, hydra_heads]
    else:
        return ["No solutions"]

print(solve())
