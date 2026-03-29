def send_over_network():
    t = int(input())  # Read the number of test cases
    for _ in range(t):
        n = int(input())  # Read the size of sequence b
        b = list(map(int, input().split()))  # Read the sequence b itself

        a = []  # Initialize an empty list to represent sequence a
        for i in range(n):
            a.append(i)  # Each segment is represented by its index + 1

        if b == a:
            print("YES")  # If sequence b matches with possible segment lengths, print YES
        else:
            print("NO")  # Otherwise, print NO

send_over_network()
