def can_send_over_network():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        
        dp = {}
        for (n, prev_val) in [(1, x) for x in b]:
            if n == 1 or prev_val > max(b):
                dp[(n, prev_val)] = 0
            else:
                dp[(n, prev_val)] = any((i < prev_val and (i+1, x) in dp) for i, x in enumerate(b))
        
        print("YES" if any(dp.values()) else "NO")

if __name__ == "__main__":
    can_send_over_network()
