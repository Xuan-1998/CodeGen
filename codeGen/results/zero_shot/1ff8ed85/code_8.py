t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    result = 'YES' if can_obtain_b_from_a([0] + [x for x in b], b) else 'NO'
    print(result)
