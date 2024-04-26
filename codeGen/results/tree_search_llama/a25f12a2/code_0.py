import sys

def find_orthus_hydra():
    heads, tails = map(int, input().split())
    for hydra in range(min(heads, tails), max(heads, tails)):
        orthus = heads - hydra
        if abs(orthus - hydra) >= 2:
            return [orthus, hydra]
    return ["No solutions"]

print(find_orthus_hydra())
