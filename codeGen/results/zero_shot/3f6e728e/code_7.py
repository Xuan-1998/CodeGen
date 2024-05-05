# Step 1: Read the input
T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    upper_rads = list(map(int, input().split()))
    lower_rads = list(map(int, input().split()))

    # Step 2: Sort the radii of the upper and lower hemispheres
    upper_rads.sort()
    lower_rads.sort()

    # Step 3: Initialize a dictionary to store the count of different sequences
    seq_count = {0: 1}
    for i in range(C):
        new_seq_count = {}
        for prev_rad, count in seq_count.items():
            if i < upper_rads[-1]:
                new_seq_count[prev_rad] = (new_seq_count.get(prev_rad, 0) + count)
            if i < lower_rads[-1]:
                new_seq_count[i+1] = (new_seq_count.get(i+1, 0) + count)
        seq_count = new_seq_count

    # Step 4: Print the result
    for i in range(C):
        print(seq_count.get(i, 0), end=' ')
    print()
