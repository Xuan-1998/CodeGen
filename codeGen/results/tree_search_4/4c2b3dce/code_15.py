def has_non_overlapping_substrings(s):
    if len(s) < 2:  # Base case: If the length of the string is less than 2, it cannot contain "AB" and "BA"
        return False

    for i in range(len(s) - 1):  # Check for "AB" substring
        if s[i:i+2] == "AB":
            remaining = s[i+2:]
            for j in range(len(remaining) - 1):  # Check for "BA" substring in the remaining part
                if remaining[j:j+2] == "BA":
                    return False
            return True

    return False

def main():
    s = input().strip()
    print("YES" if has_non_overlapping_substrings(s) else "NO")

if __name__ == "__main__":
    main()

