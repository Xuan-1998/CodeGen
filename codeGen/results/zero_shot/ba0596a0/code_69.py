stones = [int(x) for x in input().split()]

if stones[0] != 0:
    print(False)
    exit()

for i in range(1, len(stones)):
    prev_pos = stones[i-1]
    curr_pos = stones[i]
    distance = curr_pos - prev_pos
    if abs(distance) not in (k-1, k, k+1) for k in range((distance // 2) + 1)]:
        print(False)
        exit()

print(True)
