def main():
    t = int(input())  # Read the number of test cases
    for _ in range(t):
        n = int(input())  # Read the size of the sequence b
        b = list(map(int, input().split()))  # Read the sequence b
        a = [1] * (n + 1)  # Initialize the original sequence a
        for i in range(n):
            a[i+1] = abs(b[i])  # Set the segment lengths in a
        if can_generate(a, b):  # Check if b can be generated from a
            print("YES")  # Print "YES" if it's possible
        else:
            print("NO")  # Print "NO" if it's not possible

if __name__ == "__main__":
    main()
