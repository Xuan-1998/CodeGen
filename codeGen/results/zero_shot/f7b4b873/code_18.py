def find_palindromic_partitions(S):
    # TO DO: implement the logic here
    pass

if __name__ == "__main__":
    S = input()  # receive the input string from stdin
    partitions = find_palindromic_partitions(S)
    for partition in partitions:
        print(partition)  # print each palindromic partition to stdout
