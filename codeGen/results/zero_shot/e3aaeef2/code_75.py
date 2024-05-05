def apply_operation(n):
    n_str = str(n)
    new_n = ""
    for d in n_str:
        int_d = int(d) + 1
        new_n += str(int_d)
    return int(new_n)

n, m = map(int, input().split())
for _ in range(m):
    n = apply_operation(n)
print(len(str(n)) % (10**9 + 7))
