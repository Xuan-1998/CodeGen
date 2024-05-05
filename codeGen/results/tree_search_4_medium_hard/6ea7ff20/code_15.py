def solve(p):
    n = len(p) // 2
    cache = {}

    def merge_match(a, b):
        if (a and not set(b).isdisjoint(a[:])) or (b and not set(a).isdisjoint(b[:])):
            return False
        if (a and a[0] < p[n]) or (b and p[n] < b[0]):
            return merge_match([a[1:]] + [p[n]], b) if a else merge_match(a, [b[1:]] + [p[n]])
        return True

    def solve(i):
        if i >= len(p):
            return "NO"
        if (i, p[:i]) in cache:
            return cache[(i, p[:i])]
        if all(x < p[i] for x in p[:n]):
            result = merge_match(p[:n], p[n:])
        elif any(x > p[i] for x in p[n:]):
            result = "NO"
        else:
            result = solve(i + 1)
        cache[(i, p[:i])] = result
        return result

    return solve(0)

def main():
    n_cases = int(input())
    for _ in range(n_cases):
        n = int(input())
        p = list(map(int, input().split()))
        print("YES" if solve(p) else "NO")

if __name__ == "__main__":
    main()
