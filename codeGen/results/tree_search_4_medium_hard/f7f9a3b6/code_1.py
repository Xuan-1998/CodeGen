import sys

def solve():
    n = int(input())
    s = input()
    a = [int(x) for x in input().split()]

    dp = {(i, c): 0 for i in range(n+1) for c in 'abcdefghijklmnopqrstuvwxyz'}

    for i in range(1, n+1):
        for prev_char in 'abcdefghijklmnopqrstuvwxyz':
            if i <= a[ord(prev_char)-97]:
                dp[(i, prev_char)] = (dp.get((i-1, prev_char), 0) + 
                                        (dp.get((i-1, prev_char), 0) == 0)) % (10**9 + 7)
            else:
                for j in range(1, a[ord(prev_char)-97]+1):
                    dp[(i, prev_char)] = (dp.get((i-j, prev_char), 0) * 
                                            ((dp.get((j-1, chr(ord('a')+0)), 0) + 
                                              (dp.get((j-1, chr(ord('a')+0)), 0) == 0)) % (10**9 + 7)) + 
                                           dp.get((i-j, prev_char), 0)) % (10**9 + 7)
                dp[(i, prev_char)] = (dp[(i, prev_char)] + 
                                        (dp.get((i-1, prev_char), 0) == 0)) % (10**9 + 7)

    num_ways = dp[(n, 'z')]
    longest_substring_len = max(int(x[0]) for x in dp.items())
    min_substr_count = len([x for x in dp.items() if int(x[0]) > 0])

    print(num_ways)
    print(longest_substring_len)
    print(min_substr_count)

if __name__ == '__main__':
    solve()
