def checkAB(s):
    n = len(s)
    a_count = s.count('A')
    b_count = n - a_count

    if (a_count >= 1 and b_count >= 1) or (a_count <= n // 2 and b_count <= n // 2):
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    s = input()
    print(checkAB(s))
