n = int(input())
s = input()

winners = []
for i in range(2**n):
    temp = bin(i)[2:].zfill(n)
    if all(int(temp[j]) + 1 == int(s[j]) for j in range(n)):
        winners.append(temp)

print('\n'.join(sorted(winners)))
