def min_changes(s, k):
    n = len(s)
    r_count = s.count('R') % 3
    g_count = s.count('G') % 3
    b_count = s.count('B') % 3

    changes_needed = (r_count + g_count + b_count) // 3

    if k <= n:
        last_k_chars = s[-k:]
        r_count = last_k_chars.count('R') % 3
        g_count = last_k_chars.count('G') % 3
        b_count = last_k_chars.count('B') % 3

        changes_needed += (r_count + g_count + b_count) // 3

    return changes_needed


def main():
    T = int(input())
    for _ in range(T):
        n, k = map(int, input().split())
        s = input()
        print(min_changes(s, k))


if __name__ == "__main__":
    main()
