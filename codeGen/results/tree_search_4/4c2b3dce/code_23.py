def has_overlap(s):
    for i in range(len(s) - 1):
        if s[i:i+2] == "AB":
            remaining = s[i+2:]
            return has_overlap(remaining)
        elif s[i:i+2] == "BA" and (i == 0 or s[i-1] != 'B'):
            remaining = s[:i]
            return has_overlap(remaining)
    return "NO"

def main():
    s = input().strip()
    print("YES" if has_overlap(s) else "NO")

if __name__ == "__main__":
    main()
