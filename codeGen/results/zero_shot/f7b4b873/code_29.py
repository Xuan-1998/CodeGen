import sys

def is_palindrome(s):
    return s == s[::-1]

def partition_string(s):
    partitions = []
    for i in range(1, len(s) + 1):
        for j in range(len(s) - i + 1):
            partition = s[j:j+i]
            if is_palindrome(partition):
                partitions.append([partition])
                for k in range(i-1, 0, -1):
                    new_partition = s[j+k:j+i+k]
                    if is_palindrome(new_partition):
                        partitions[-1].append(new_partition)
    return partitions

def main():
    s = sys.stdin.readline().strip()
    result = partition_string(s)
    print(result)

if __name__ == "__main__":
    main()
