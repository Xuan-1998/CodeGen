a, b = map(int, input().split())
result = []
for i in range(a, b+1):
    if str(i) == ''.join(str(int(x)**(i_digits.index(x)+1)) for x in set(str(i))):
        result.append(i)
print(' '.join(map(str, sorted(result))))
