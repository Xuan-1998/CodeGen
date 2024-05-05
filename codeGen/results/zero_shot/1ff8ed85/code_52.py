import random

for _ in range(10):
    n = random.randint(1, 10000)
    b = [random.randint(1, 1000000) for _ in range(n)]
    
    print(f"{n} {' '.join(map(str, b))}")
