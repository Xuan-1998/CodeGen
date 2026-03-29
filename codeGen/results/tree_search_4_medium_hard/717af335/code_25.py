def find_x(a, b):
    has_solution = {(0, 0): True}

    def dfs(i, j):
        if (i, j) not in has_solution:
            has_solution[(i, j)] = False

        if i > 0 or j > min(a, b):
            return False
        elif i == a and j == b:
            return True
        else:
            has_solution[(i, j)] = (dfs(max(0, i - j), min(j, a)) or dfs(min(i, b), max(0, j - i)))
            return has_solution[(i, j)]

    if a > 1 and b == 0:
        return -1
    elif a == 1 and b > 0:
        return -1

    if dfs(a, b):
        x = (a + b) // 2
        y = max(0, a - x)
        return str(x) + " " + str(y)
    else:
        return "-1"
