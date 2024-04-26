def count_bear_substrings():
    s = input()  # receive the input string from stdin

    bear_length = len('bear')  # length of the word "bear"
    bear_count = 0  # initialize the count of substrings containing "bear"

    for i in range(len(s) - bear_length + 1):  # iterate over all possible substrings
        substring = s[i:i+bear_length]  # extract the current substring
        if substring == 'bear':  # check if the substring contains the word "bear"
            bear_count += 1  # increment the count

    print(bear_count)  # print the result to stdout

count_bear_substrings()
