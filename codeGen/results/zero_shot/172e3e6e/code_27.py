n = int(input())  # read the length of the array and the array itself
a = list(map(int, input().split()))  # convert the input string to an integer array

result = count_good_subsequences(a)
print(result)  # print the result modulo 10^9 + 7
