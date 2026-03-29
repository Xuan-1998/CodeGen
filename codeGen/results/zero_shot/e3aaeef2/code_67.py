import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    # Initialize a set to store the numbers
    num_set = {n}
    for _ in range(m):
        new_num_set = set()
        for num in num_set:
            temp = ''
            carry = 0
            for digit in str(num):
                d = int(digit) + 1
                if d > 9: 
                    d, carry = divmod(d, 10)
                    if carry: break
                temp += str(d)
            else:
                new_num_set.add(int(temp))
        num_set = new_num_set
    print(len(str(max(num_set))) % (10**9 + 7))
