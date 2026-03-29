import sys

def is_palindrome(s):
    return s == s[::-1]

def generate_partitions(s, partitions=None, start=0):
    if partitions is None:
        partitions = []
    if start == len(s):
        result.append(partitions)
        return
    for end in range(start + 1, len(s) + 1):
        partition = s[start:end]
        if is_palindrome(partition):
            generate_partitions(s, partitions + [partition], end)

def main():
    S = sys.stdin.readline().strip()
    result = []
    generate_partitions(S)
    print(result)

if __name__ == "__main__":
    main()
