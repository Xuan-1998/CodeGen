radii_count = {}
total_count = 0

for _ in range(int(input())):
    N, M, C = map(int, input().split())
    for _ in range(N):
        radius = int(input())
        if radius not in radii_count:
            radii_count[radius] = 1
        else:
            radii_count[radius] += 1

    for _ in range(M):
        radius = int(input())
        if radius not in radii_count:
            radii_count[radius] = 1
        else:
            radii_count[radius] += 1

    total_count = len(radii_count)
    
    for i in range(1, C+1):
        upper_count = sum(radii_count[j] for j in range(1, i+1))
        lower_count = sum(radii_count[k] for k in range(i, C+1))
        print((upper_count * lower_count) % (10**9 + 7), end=' ')
    print()
