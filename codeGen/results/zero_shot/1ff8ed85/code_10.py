def can_send_sequence():
    t = int(input())  # number of test cases
    for _ in range(t):
        n = int(input())  # size of sequence b
        b = list(map(int, input().split()))  # sequence b

        a = [0] * (n + 1)  # initialize a with zeros
        for i in range(1, n + 1):
            if b[i - 1] > a[i - 1]:  # if current element in b is greater than the previous one
                a[i] = b[i - 1] - a[i - 1]  # add the difference to the corresponding position in a
            else:  # if current element in b is less than or equal to the previous one
                a[i] = a[i - 1] - b[i - 1]  # subtract the difference from the corresponding position in a

        print("YES" if all(a[i] >= 0 for i in range(1, n + 1)) else "NO")  # check if all elements in a are non-negative

if __name__ == "__main__":
    can_send_sequence()
