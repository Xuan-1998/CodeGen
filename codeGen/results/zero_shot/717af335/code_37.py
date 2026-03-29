def find_solution():
    A = int(input())
    B = int(input())

    # Find the smallest possible value for X that satisfies the conditions
    X = min(A, (B + 1) // 2)
    
    if X * 2 == A:
        Y = A - X
    else:
        return -1

    return f"{X} {A - X}"

print(find_solution())
