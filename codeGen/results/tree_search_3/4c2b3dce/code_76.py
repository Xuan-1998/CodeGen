def check_abba(s):
    count_a = 0
    count_b = 0

    for char in s:
        if char == 'A':
            count_a += 1
        elif char == 'B':
            count_b += 1

    return "YES" if (count_a > 0 and count_b > 0) else "NO"

s = input()
print(check_abba(s))
