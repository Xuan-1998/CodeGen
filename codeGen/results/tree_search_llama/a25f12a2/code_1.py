from math import comb

def count_creatures():
    h, t = map(int, input().split())
    
    if h + t < 2 or h > 1000 or t > 1000:
        print("No solutions")
        return
    
    total_count = [0] * (h+1)
    for i in range(1, h+1):
        total_count[i] = comb(i-1, 0) * comb(t-i*3-2, 2)
    
    orthus_count = sum(total_count[:i+1] for i in range(h//3+1))
    hydra_count = sum(total_count[i+1:] for i in range(h//3))
    
    if h == 0:
        print([hydra_count // 3, hydra_count % 3])
    elif t == 0:
        print([orthus_count // 3, orthus_count % 3])
    else:
        print([orthus_count // 3, orthus_count % 3] if h > 2*orthus_count + 2*t else [hydra_count // 3, hydra_count % 3])

count_creatures()
