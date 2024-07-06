import sys

def main():
    # Read input
    t = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    strings = [sys.stdin.readline().strip() for _ in range(n)]

    # Preprocessing: Calculate the length of each string
    string_lengths = {i: len(s) for i, s in enumerate(strings)}

    # Initialize variables to track the number of steps and last used index
    steps = 0
    last_used_index = -1

    # Iterate through the text
    for i in range(len(t)):
        found = False
        for j in range(n):
            if t[i:i + string_lengths[j]].lower() == strings[j].lower():
                # Found a match, mark characters as 'red' and update variables
                steps += 1
                last_used_index = j
                found = True
                break

        # If no matches were found in the current step, exit the loop
        if not found:
            break

    # Print output
    print(steps)
    for _ in range(steps):
        print(last_used_index + 1)

if __name__ == "__main__":
    main()
