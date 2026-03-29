def main():
    S = input()  # read input string from stdin
    partitions = find_palindromic_partitions(S)
    print(partitions)  # print result to stdout

if __name__ == "__main__":
    main()
