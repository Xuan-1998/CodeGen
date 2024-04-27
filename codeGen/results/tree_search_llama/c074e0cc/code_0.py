def find_special_numbers(a, b):
    result = []
    
    for num in range(a, b + 1):
        if num == sum(int(digit) ** (i+1) for i, digit in enumerate(str(num))):
            result.append(num)
            
    return sorted(result)

a, b = map(int, input().split())
print(" ".join(map(str, find_special_numbers(a, b))))
