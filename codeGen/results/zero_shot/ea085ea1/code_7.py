import sys
import uffdsa as utf

N = int(input())
str1 = input().strip()
str2 = input().strip()

utf1 = utf.SuffixTree(str1)
utf2 = utf.SuffixTree(str2)

common_substrings = []
for node1 in utf1:
    for node2 in utf2:
        if node1 == node2:
            common_substring = str1[node1.begin:node1.end]
            common_substrings.append(common_substring)

max_common_substrings = len(set(common_substrings))
print(max_common_substrings)
