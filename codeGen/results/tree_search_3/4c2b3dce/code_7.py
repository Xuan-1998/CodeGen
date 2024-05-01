def can_split(s):
    if not s:
        return "NO"

    def helper(s):
        if not s:
            return True

        for i in range(len(s) - 2):
            if s[i:i+2] == "AB" and s[i+2:] == "BA":
                return True
            elif s[i:i+2] == "BA" and s[:i] == "AB":
                return True

        return False

    return "YES" if helper(s) else "NO"


if __name__ == "__main__":
    s = input()
    print(can_split(s))
