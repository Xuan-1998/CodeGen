def merge(a, b):
    result = []
    while a and b:
        if a[0] <= b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
    result.extend(a or b)
    return result

def solve(n, p):
    memo = {}

    def dfs(i, a, b):
        if i >= n * 2:
            return "YES" if sorted(p[:i]) == sorted(p[i:]) else "NO"
        if (a, b, i) in memo:
            return memo[(a, b, i)]
        if not a and not b:
            return "YES"
        if not a or not b:
            p.extend(a or b)
            return dfs(i + len(a or b), [], [])
        if a[0] <= b[0]:
            p.append(a.pop(0))
            result = dfs(i + 1, a, b)
            memo[(a, b, i)] = result
            return result
        else:
            p.append(b.pop(0))
            result = dfs(i + 1, a, b)
            memo[(a, b, i)] = result
            return result

    return "YES" if dfs(0, list(range(n)), list(range(n))) == "YES" else "NO"


def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    print(solve(n, p))


if __name__ == "__main__":
    main()
