import sys

def main():
    s = sys.stdin.readline().strip()
    
    ab_count = 0
    ba_count = 0
    
    for i in range(len(s) - 1):
        if s[i:i+2] == 'AB' or s[i:i+2] == 'BA':
            if s[i:i+2] == 'AB':
                ab_count += 1
            else:
                ba_count += 1
                
    if ab_count == 1 and ba_count == 1:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
