def find_orthus_hydra(heads, tails):
    if heads + tails < 2 or heads > tails + 2:
        return "No solutions"
    
    for orthus in range(min(heads, tails), max(heads, tails) // 2, -1):
        hydra = heads - orthus
        if abs(orthus - hydra) >= 2:
            return [orthus, hydra]
    
    return "No solutions"
