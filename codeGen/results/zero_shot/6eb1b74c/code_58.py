import sys

def solve():
    t = input().strip()
    n = int(input())
    s_dict = {}
    for _ in range(n):
        s = input().strip()
        if s not in s_dict:
            s_dict[s] = len(s)

    steps = 0
    used_strings = []
    while True:
        max_prefix_len = 0
        covering_s = None
        for s, length in s_dict.items():
            prefix_len = 0
            while True:
                if t[:prefix_len+length].endswith(s):
                    prefix_len += 1
                else:
                    break
            if prefix_len > max_prefix_len:
                max_prefix_len = prefix_len
                covering_s = s
        if covering_s is None:
            print(-1)
            return

        steps += 1
        used_strings.append((s_dict[covering_s], len(t) - max_prefix_len))
        t = t[:max_prefix_len] + '#' * (len(t) - max_prefix_len)

    print(steps)
    for s, p in used_strings:
        print(f"{s} {p}")

if __name__ == "__main__":
    solve()
