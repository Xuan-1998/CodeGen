n, q = map(int, input().split())
signs = list(input())

for _ in range(q):
    l, r = map(int, input().split())
    
    total_signs = sum(signs[l:r+1])
    odd_counts = 0

    cumulative_signs = [0] * (n + 1)
    for i, sign in enumerate(signs):
        cumulative_signs[i+1] = cumulative_signs[i] + sign

    total_signs_in_range = cumulative_signs[r+1] - cumulative_signs[l]
    odd_counts = (total_signs_in_range + len(range(l, r+1)) % 2)
    print(odd_counts)
