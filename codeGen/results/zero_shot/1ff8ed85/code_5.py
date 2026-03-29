def can_send(a, b):
    stack = []
    i = 0
    while i < len(b):
        j = i + 1
        while j <= len(b) and int(str(b[i]) + str(j)) <= max(a):
            j += 1
        if j - i > 1:
            stack.append((i, j - 1))
        i = j
    for segment in stack:
        a = a[:segment[0]] + [str(segment[0] + len(str(segment[1])))] + a[segment[1]+1:]
    return "".join(map(str, a)) == "".join(map(str, b))
