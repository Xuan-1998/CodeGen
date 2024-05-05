def min_changes_to_match(k):
    while True:
        r_count = 0
        g_count = 0
        b_count = 0

        s = input().strip()
        n = len(s)

        if n < k:
            return -1

        for char in s:
            if char == 'R':
                r_count += 1
            elif char == 'G':
                g_count += 1
            else:
                b_count += 1

        min_changes = max(r_count, g_count, b_count) - (n // k)
        print(min_changes)

