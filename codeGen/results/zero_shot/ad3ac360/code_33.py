def minCuts(s):
    n = len(s)
    min_cuts = n - 1

    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            if substring != substring[::-1]:
                min_cuts += 1
                break

    return min_cuts

if __name__ == "__main__":
    s = input()
    print(minCuts(s))
