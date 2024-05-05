t = int(input())  # read the number of test cases

for _ in range(t):
    n = int(input())  # read the size of the sequence b
    b = list(map(int, input().split()))  # read the sequence b

    a = []  # initialize the sequence a
    for i in range(n):
        if a and abs(b[i] - len(str(len(a) + 1))) <= abs(b[i] - len(str(len(a)))):
            a.append(len(a) + 1)
        else:
            a.append(i + 1)

    if b == [len(x) for x in (str(len(a)) for _ in range(n))]:
        print("YES")  # sequence b can be obtained from sequence a
    else:
        print("NO")  # sequence b cannot be obtained from sequence a
