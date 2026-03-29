def get_partitions(s):
    n = len(s)
    if n == 0:
        return [[]]

    partitions = []
    for i in range(n):
        prefix = s[:i+1]
        suffix = s[i+1:]
        remaining_partitions = get_partitions(suffix)

        # Check if the current prefix can be appended to the right side of an existing partition
        for j, partition in enumerate(remaining_partitions):
            new_partition = [prefix] + partition
            partitions.append(new_partition)

    return partitions

def main():
    s = input()
    partitions = get_partitions(s)
    print(partitions)

if __name__ == "__main__":
    main()
