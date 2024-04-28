import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

winners = []
for i in range(2**n):
    temp = bin(i)[2:].zfill(n)
    if all((t == '1' and c == '0') or (t == '0' and c == '1') for t, c in zip(temp, s)):
        winners.append(i)

print(*winners, sep='\n')
