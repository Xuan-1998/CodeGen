heads, tails = map(int, input().split())
orthus_heads = min(heads // 2 + 1, heads)
hydra_heads = heads - orthus_heads
hydra_tails = min(tails // 3 + 1, tails)

if hydra_heads * 3 >= tails and hydra_heads <= hydra_tails:
    print([orthus_heads, hydra_heads * 3])
else:
    print("No solutions")
