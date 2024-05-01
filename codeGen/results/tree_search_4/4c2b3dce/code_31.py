===
while True:
    try:
        s = input().upper()
        break
    except EOFError:
        pass

seen_AB = False
for i in range(len(s)):
    if s[i:i+2] == 'AB':
        seen_AB = True
    elif seen_AB and s[i:i+2] == 'BA' and i + 2 >= len(s):
        print("YES")
        exit(0)

print("NO")
