def f(s):
    p = min((i for i in range(2, s + 1) if all(i % j > 0 for j in [s // i] + [j for j in a])))
    return f(s // p) - (s // p) if p not in b else f(s // p) + (s // p)

max_beauty = max(f(x) for x in range(1, n + 1))

# Print the answer to stdout
print(max_beauty)
