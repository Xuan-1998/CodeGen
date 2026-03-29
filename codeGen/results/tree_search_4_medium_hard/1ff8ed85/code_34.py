import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        b = list(map(int, sys.stdin.readline().split()))
        a_freq = {}
        cum_sum = 0
        prev_val = -1
        for val in sorted(b):
            if val > prev_val + 1:
                cum_sum += 1
            else:
                cum_sum += (val - prev_val) if prev_val != -1 else 1
            a_freq[val] = a_freq.get(val, 0) + 1
            prev_val = val

        seg_count = 0
        for i in range(1, n):
            if b[i] > cum_sum:
                break
            cum_sum += 1
            seg_count += 1

        print("YES" if seg_count == len(b) else "NO")

if __name__ == "__main__":
    solve()
