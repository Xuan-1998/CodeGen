def can_obtain_b(a, b):
    b.sort()
    for num in b:
        found = False
        temp_sum = 0
        for seg_len in a:
            if temp_sum + seg_len <= num:
                temp_sum += seg_len
            else:
                break
        if temp_sum == num:
            continue
        else:
            return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(can_obtain_b(a, b))
