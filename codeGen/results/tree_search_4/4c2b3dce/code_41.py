def solve():
    s = input().strip()
    has_ab = False
    for i in range(len(s) - 1):
        if s[i] == 'A' and s[i + 1] == 'B':
            has_ab = True
            break

    if not has_ab:
        return "NO"

    has_ba = False
    remaining_string = s[len(s) - len(s) // 2:]
    for i in range(len(remaining_string) - 1):
        if remaining_string[i] == 'B' and remaining_string[i + 1] == 'A':
            has_ba = True
            break

    return "YES" if has_ab and has_ba else "NO"
