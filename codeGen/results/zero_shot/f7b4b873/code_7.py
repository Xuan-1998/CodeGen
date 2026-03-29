def is_palindrome(substring):
    return substring == substring[::-1]

def get_partitions(s):
    if len(s) == 0:
        return [[]]

    partitions = []
    for i in range(1, len(s)):
        first_partition = s[:i]
        remaining_string = s[i:]
        if is_palindrome(first_partition):
            for p in get_partitions(remaining_string):
                partitions.append([first_partition] + p)
    return partitions

def main():
    s = input()
    partitions = get_partitions(s)
    for p in partitions:
        print(p)

if __name__ == "__main__":
    main()
