def solve():
    s = input()
    count_a = 0
    count_b = 0

    for char in s:
        if char == 'A':
            count_a += 1
        elif char == 'B':
            count_b += 1

    if (count_a + 1) % 2 != 0 and (count_b + 1) % 2 != 0:
        print("YES")
    else:
        print("NO")

solve()
