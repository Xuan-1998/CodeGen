import sys

def main():
    s = input().strip()
    if len(s) < 2:
        print("NO")
        return
    elif set(s).issubset({'A', 'B'}):
        print("NO")
        return
    
    for i in range(len(s) - 1):
        if s[i:i+2] == "AB" or s[i:i+2] == "BA":
            remaining = s[i+2:]
            if (remaining.find('A') != -1 and remaining.find('B') != -1 and
               abs(remaining.find('A') - remaining.find('B')) > 1):
                print("YES")
                return
    print("NO")

if __name__ == "__main__":
    main()
