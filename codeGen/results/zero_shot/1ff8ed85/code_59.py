def can_send_over_network():
    t = int(input())  # Read the number of test cases

    for _ in range(t):
        n = int(input())  # Read the size of sequence b
        b = list(map(int, input().split()))  # Read the integers in sequence b

        a = ""  # Initialize an empty string to store the modified sequence

        for i in range(n - 1):
            diff = abs(b[i] - b[i + 1])  # Calculate the absolute difference between two consecutive numbers
            if diff == b[i]:  # If it's equal to the length of a segment
                a += "+" + str(diff)  # Add the segment boundary notation and segment length
            elif diff == b[i + 1]:
                a += "-" + str(diff)
            else:
                a += str(b[i]) + " "  # Otherwise, just add the number with a space

        if a != str(b).replace(" ", ""):  # Check if we can obtain sequence b from some sequence a
            print("YES")
        else:
            print("NO")

can_send_over_network()
