import sys
input = sys.stdin.read().split()
T = int(input[0])
for _ in range(T):
    N = int(input[_+1])
    count_carry = 0
    for a in range(10**(N-1), 10**N):
        for b in range(10**(N-1), 10**N):
            carry = sum(int(d1) + int(d2) >= 10 for d1, d2 in zip(str(a)[::-1], str(b)[::-1])) // (2*9)
            count_carry += carry
    print(count_carry/(10**N)**2)
