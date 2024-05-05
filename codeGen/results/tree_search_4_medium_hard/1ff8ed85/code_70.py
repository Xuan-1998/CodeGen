t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    dp = {}
    
    def can_send_b(i, p):
        if i >= n:
            return True
        if (i, tuple(p)) in dp:
            return dp[(i, tuple(p))]
        ans = False
        for a_len in range(1, min(len(b) - i, len(p) + 1)):
            for val in range(min(b[i], a_len), max(b[i] + 1, a_len) + 1):
                if (i + a_len, p + [val]) and can_send_b(i + a_len, p + [val]):
                    ans = True
                    break
        dp[(i, tuple(p))] = ans
        return ans
    
    print("YES" if can_send_b(0, []) else "NO")
