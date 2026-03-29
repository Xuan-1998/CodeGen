code
import sys
n, k = map(int, input().split())
s = input()
if k <= n:
    if k == 1: 
        print(s[k-1])  # printing the character at index (k-1) because indexing in python starts from 0
    elif s[:k] < s[1:k+1]:  # checking if the string till index k is smaller than the string after skipping the first character and till the end of the string
        print(s[:k])  # printing the smallest possible string which can be obtained by either deleting the last character or duplicating the string
    else:
        print(s[1:k+1])  # printing the second smallest possible string which is one character longer than the first one and can also be achieved by either deleting the last character or duplicating the string
else:
    if k == n + 1: 
        print(s)  # when we want to duplicate the whole string, just return the original string
    elif s < s+s[:n-k+1]:  # checking if the string is smaller than its duplication plus the remaining part of the string after skipping the first k characters
        print(s)  # printing the smallest possible string which can be obtained by either deleting the last character or duplicating the string
    else:
        print(s+s[:n-k+1])  # printing the second smallest possible string which is one more than the length of the original string and can also be achieved by either deleting the last character or duplicating the string
