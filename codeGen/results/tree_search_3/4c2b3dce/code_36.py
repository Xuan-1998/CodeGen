import sys

def find_ab_sba(s):
    found_a = False
    found_b = False

    for c in s:
        if not found_a and c == 'A':
            found_a = True
        elif found_a and c == 'B':
            found_b = True
            break  # found both substrings, exit the loop
        elif found_b and c == 'A':
            found_b = False  # reset found_b since we've seen 'A' again

    if found_a and found_b:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    find_ab_sba(s)
