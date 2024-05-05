def max_value(sequence):
    n = len(sequence) + 1
    terminated = False
    y = 0

    for x in range(2, n+1):
        a_x = sequence[x-2]
        while x+a_x > n or x <= 0:
            if x <= 0:
                terminated = True
                break
            x += sequence[x-2]

        if terminated:
            return -1

        y += a_x
        x += a_x

    return y
