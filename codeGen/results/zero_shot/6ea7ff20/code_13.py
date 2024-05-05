def solution():
    n = int(input())  # read n from standard input
    p = list(map(int, input().split()))  # read permutation p

    a = []  # initialize arrays a and b
    b = []
    i = 0
    while i < len(p):
        if not a or p[i] > a[-1]:
            a.append(p[i])
        else:
            b.append(p[i])
        i += 1

    if len(a) + len(b) != len(p):  # check if permutation length matches
        print("NO")
    elif any(x in b for x in a):  # check if arrays have common elements
        print("NO")
    else:
        print("YES")

if __name__ == "__main__":
    solution()
