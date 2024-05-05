code = """
n, k, z = map(int, input().split())
score = 0
direction = 1

for i in range(1, n+1):
    if direction == 1: # moving right
        score += [1]*k[i-1]
    else: # moving left
        score -= [1]*z
    direction *= -1

print(score)
"""
