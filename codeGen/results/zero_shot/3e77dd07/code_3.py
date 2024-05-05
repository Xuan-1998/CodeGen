class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def stringToTree(s):
    if not s:
        return None
    
    root = Node(s[0])
    node = root
    for char in s[1:]:
        if char == 'A':
            node.right = Node(char)
            node = node.right
        else:
            node.left = Node(char)
            node = node.left
    return root

def isIsomorphic(t1, t2):
    if not t1 or not t2:
        return False
    
    def treeToDict(node):
        if not node:
            return {}
        
        left_dict = treeToDict(node.left)
        right_dict = treeToDict(node.right)
        
        if node.value in left_dict and node.value in right_dict:
            return {node.value: 'B'}
        elif node.value in left_dict:
            return {node.value: 'L' + str(left_dict.get(node.value, 0))}
        elif node.value in right_dict:
            return {node.value: 'R' + str(right_dict.get(node.value, 0))}
        else:
            return {node.value: 'L0' if not left_dict else 'R' + str(left_dict.get('root', 0))}
    
    t1_dict = treeToDict(t1)
    t2_dict = treeToDict(t2)
    
    return t1_dict == t2_dict

def main():
    s1, s2 = input().split()
    root1 = stringToTree(s1)
    root2 = stringToTree(s2)
    
    if isIsomorphic(root1, root2):
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()
