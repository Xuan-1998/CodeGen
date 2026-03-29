def can_form_sequence(b):
    n = len(b)
    for seg_len in range(1, n+1):
        seg_sum = 0
        for i in range(0, n, seg_len):
            if i + seg_len > n:
                break
            seg_sum += seg_len
            if seg_sum * 2 != n and (seg_sum + b[i:i+seg_len]) != n:
                return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    print("YES" if can_form_sequence(b) else "NO")
