import sys

test_cases = []
while True:
    t = input().strip()
    n = int(input())
    test_case = [t, n]
    for _ in range(n):
        s_i = input().strip()
        test_case.append(s_i)
    test_cases.append(test_case)

for test_case in test_cases:
    m = 0
    steps = []
    for s_i in test_case[1:]:
        occurrences = [(i, test_case[0].find(s_i)) for i in range(len(test_case[0])) if test_case[0].find(s_i) != -1]
        if not occurrences:  # no occurrences found
            print(-1)
            sys.exit()
        steps_needed = len(occurrences)
        m += steps_needed

    print(m)
    for i in range(m):
        w_i = test_case[1:][i].index(min(test_case[1:][i]))
        p_i = occurrences[w_i][0]
        print(f"{w_i+1} {p_i+1}")
