t = int(input())  # read the number of test cases

for _ in range(t):
    n = int(input())  # read the size of the sequence
    b = list(map(int, input().split()))  # read the sequence b
    a = [0] * (n + 1)  # initialize the sequence a with zeros
    for i in range(n):
        a[i + 1] = a[i] + b[i]  # calculate the cumulative sum of sequence b
    for i in range(1, n + 1):  # iterate through the sequence b
        if not (a[i - 1] == a[i] or a[n - i]):
            print("NO")  # if we can't obtain the segment by splitting a, print NO
            break
    else:
        print("YES")  # if we can obtain all segments by splitting a, print YES
