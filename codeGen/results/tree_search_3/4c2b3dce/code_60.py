code = codeblock
from sys import stdin

input_string = stdin.readline().strip()
if len(input_string) == 0:
    print("NO")
elif ('AB' in input_string and 'BA' not in input_string) or ('BA' in input_string and 'AB' not in input_string):
    print("NO")
else:
    found_AB = False
    for i in range(len(input_string) - 1):
        if input_string[i:i+2] == 'AB':
            found_AB = True
            break
    if found_AB:
        remaining_string = input_string[len('AB'):]
        if 'BA' in remaining_string:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

