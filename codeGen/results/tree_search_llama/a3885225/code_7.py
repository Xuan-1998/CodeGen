def can_convert_to_palindrome():
    n = int(input())
    s = input()
    
    zero_count = 0
    one_count = 0
    
    for char in s:
        if char == '0':
            zero_count += 1
        else:
            one_count += 1
        
    left, right = 0, n - 1
    
    while left <= right:
        if s[left] != s[right]:
            if zero_count > one_count and s[left] == '1':
                return "NO"
            elif one_count > zero_count and s[right] == '1':
                return "NO"
            else:
                break
        left += 1
        right -= 1
        
    if (zero_count - one_count) % 2 == 0 or (one_count - zero_count) % 2 == 0:
        return "YES"
    else:
        return "NO"


while True:
    try:
        print(can_convert_to_palindrome())
    except:
        break
