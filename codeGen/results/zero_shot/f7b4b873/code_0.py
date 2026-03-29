def main():
    s = input()  # read input from stdin
    partitions = palindrome_partitions(s)
    for partition in partitions:
        print(partition)

if __name__ == "__main__":
    main()
