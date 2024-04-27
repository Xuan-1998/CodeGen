def can_be_palindrome():
    n = int(input())
    s = input()
    
    freq = {'0': 0, '1': 0}
    for char in s:
        if char in freq:
            freq[char] += 1
    
    if abs(freq['0'] - freq['1']) > 1:
        print('NO')
    else:
        print('YES')

if __name__ == '__main__':
    can_be_palindrome()
