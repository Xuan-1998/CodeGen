code
n = int(input())
result = 0

for _ in range(n):
    row = input()
    
    for i in range(len(row)):
        if row[i] == '.':
            j = i + 1
            while j < len(row) and row[j] == '.':
                j += 1
            
            if all(row[k] == '.' for k in range(i+1, j)):
                result += 1

print(result)
