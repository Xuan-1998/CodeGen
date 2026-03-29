class Node:
    def __init__(self, char):
        self.char = char
        self.left = None
        self.right = None

def stringToTree(s):
    if not s:
        return None
    
    root = Node(s[0])
    queue = [root]
    
    i = 1
    while i < len(s) and queue:
        current = queue.pop(0)
        
        left_char = s[i]
        right_char = s[i+1] if i+1 < len(s) else ''
        
        current.left = Node(left_char) if left_char else None
        current.right = Node(right_char) if right_char else None
        
        if i+1 < len(s):
            queue.append(current.left)
            queue.append(current.right)
        
        i += 2
    
    return root

def treeToString(node):
    if not node:
        return ''
    
    result = str(node.char)
    queue = [node]
    
    while queue:
        current = queue.pop(0)
        
        if current.left:
            result += treeToString(current.left)[1:]
            queue.append(current.left)
        if current.right:
            result += treeToString(current.right)[1:]
            queue.append(current.right)
    
    return result

def isScrambled(s1, s2):
    if len(s1) != len(s2):
        return False
    
    t1 = stringToTree(s1)
    t2 = stringToTree(s2)
    
    return treeToString(t1) == treeToString(t2)

# Input
s1 = input()
s2 = input()

# Call the function to check if s2 is a scrambled version of s1
result = isScrambled(s1, s2)

# Output
print(result)
