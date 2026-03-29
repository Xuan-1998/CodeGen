def partition_palindromes(s):
    def is_palindrome(s):
        return s == s[::-1]

    def generate_partitions(s, current_partition=None):
        if current_partition is None:
            current_partition = []
        partitions = [current_partition]
        for i in range(len(s)):
            new_partition = current_partition + [s[i]]
            for j in range(i+1, len(s)+1):
                new_string = s[i:j]
                if is_palindrome(new_string):
                    new_partition.append(new_string)
                    yield from generate_partitions(new_string, new_partition)
        yield partitions

    return list(generate_partitions(s))

def main():
    s = input()
    result = partition_palindromes(s)
    print(result)

if __name__ == "__main__":
    main()
