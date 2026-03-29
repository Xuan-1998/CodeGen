A = int(input())  # read A from stdin
B = int(input())  # read B from stdin

x, y = find_X_and_Y(A, B)

if x == -1:
    print(-1)  # no solution found
else:
    print(x, y)  # print the solution
