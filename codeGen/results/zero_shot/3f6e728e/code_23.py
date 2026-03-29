# Step 1: Read the input
T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    upper_radii = list(map(int, input().split()))
    lower_radii = list(map(int, input().split()))

    # Step 2: Sort the radii of both hemispheres
    upper_radii.sort()
    lower_radii.sort()

    # Step 3: Initialize a prefix sum array for the upper hemispheres and count the number of different X-sequences
    upper_prefix_sum = [0] * (C + 1)
    for i in range(N):
        upper_prefix_sum[upper_radii[i]] += 1

    lower_prefix_sum = [0] * (C + 1)
    for i in range(M):
        lower_prefix_sum[lower_radii[i]] += 1

    # Step 4: Calculate the number of different X-sequences
    x_sequences = 1
    for i in range(1, C + 1):
        upper_count = upper_prefix_sum[i]
        lower_count = lower_prefix_sum[i]
        if upper_count > 0 and lower_count > 0:
            x_sequences *= (upper_count * lower_count) % (10**9 + 7)
    print(x_sequences % (10**9 + 7))
