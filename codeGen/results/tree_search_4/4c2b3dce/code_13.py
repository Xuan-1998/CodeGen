import sys

input_string = input().strip()

dp = [False] * (len(input_string) + 1)

for i in range(1, len(input_string) + 1):
    dp[i] = False
    for j in range(i):
        if ((i - j > 0 and dp[i - j]) or 
            (input_string[j:j+2] == "AB" or input_string[j:j+2] == "BA") and 
            (j < i - 2 or input_string[i-1:i+1] != "AB" and input_string[i-1:i+1] != "BA")):
            dp[i] = True
            break

if dp[-1]:
    print("YES")
else:
    print("NO")
