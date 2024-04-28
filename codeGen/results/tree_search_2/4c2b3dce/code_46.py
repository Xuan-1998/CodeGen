def check_string():
    s = input()
    count_a = 0
    count_b = 0

    for c in s:
        if c == 'A':
            count_a += 1
        elif c == 'B':
            count_b += 1

    if (count_a - count_b) % 2 == 1 or (count_a + count_b) % 3 != 0:
        print("YES")
    else:
        print("NO")

check_string()
