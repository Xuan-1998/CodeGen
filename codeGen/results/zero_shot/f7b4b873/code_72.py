def partition(s):
    if not s:
        return []

    partitions = []
    for i in range(1, len(s)):
        prefix = s[:i]
        suffix = s[i:]
        if prefix == suffix and prefix:
            parts = [prefix] + partition(suffix)
            partitions.append(parts)

    return partitions

def main():
    S = input()  # read the input string from stdin
    partitions = partition(S)
    for p in partitions:
        print(p)  # print each palindromic partition

if __name__ == "__main__":
    main()
