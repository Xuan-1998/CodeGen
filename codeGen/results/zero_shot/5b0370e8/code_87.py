import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        and_counts = {}
        for _ in range(n):
            x = int(input())
            if x not in and_counts:
                and_counts[x] = 0
            and_counts[x] += 1
        
        xor_sum = 0
        for x in and_counts:
            xor_sum ^= x * and_counts[x]
        
        and_count = sum(2**i - 1 for i in range(k.bit_length()) if (1 << i) & x)
        if xor_sum > 0:
            ans = (and_count + 1) % (10**9 + 7)
        else:
            ans = and_count % (10**9 + 7)
        
        print(ans)

if __name__ == "__main__":
    solve()
