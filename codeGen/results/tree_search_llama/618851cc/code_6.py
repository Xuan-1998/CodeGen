def find_solution():
    a_min = min(map(int, input().split()))
    b_min = min(map(int, input().split()))

    A = sorted(map(int, input().split()))
    B = sorted(map(int, input().split()))

    merged_array = list(set(A + B))  # Use set to remove duplicates

    for a in range(a_min, max(A) + 1):
        for b in range(b_min, max(B) + 1):
            if A.index(a) < len(A) and B.index(b) < len(B) and (a + b) not in A and (a + b) not in B:
                return str(a) + ' ' + str(b)

    print("No solution found.")

find_solution()
