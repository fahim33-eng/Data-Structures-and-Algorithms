class Node :
    def __init__(self, num) :
        self.value = num
        self.left = None
        self.right = None
        self.height = 1

class AVL :
    def height(self, node) :
        if node is None :
            return 0
        else :
            return node.height
    def balance(self, node) :
        if node is None :
            return 0
        else :
            return self.height(node.left) - self.height(node.right)
        
    def minVal(self, node) :
        if node.left is None :
            return node.value
        else :
            return self.minVal(node.left)
        
    def rotateR(self, root) :
        a = root.left
        b = a.right
        a.right = root
        root.left = b
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        a.height = 1 + max(self.height(a.left), self.height(a.right))
        return a 
    
    def rotateL(self, root) :
        a = root.right
        b = a.left
        a.left = root
        root.right = b
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        a.height = 1 + max(self.height(a.left), self.height(a.right))
        return a
    
    def insert(self, val, node) :
        if node is None :
            return Node(val)
        if val == node.value :
            return
        elif val < node.value :
            node.left = self.insert(val, node.left)
        else :
            node.right = self.insert(val, node.right)
            
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.balance(node)
        
        if balance > 1 and node.left.value > val :
            return self.rotateR(node)
        if balance < -1 and val > node.right.value :
            return self.rotateL(node)
        if balance > 1 and val > node.left.value  :
            node.left = self.rotateL(node.left)
            return self.rotateR(node)
        if balance < -1 and val < node.right.value  :
            node.right = self.rotateR(node.right)
            return self.rotateL(node)
        return node
    
    def inOrder(self, node) :
        if node is None :
            return
        self.inOrder(node.left)
        print(node.value)
        self.inOrder(node.right)
        
    def delete(self, val, node) :
        if node is None :
            return None
        elif val < node.value :
            node.left = self.delete(val, node.left)
        elif val > node.value :
            node.right = self.delete(val, node.right)
        else :
            if node.left is None :
                lt = node.right
                node = None
                return lt
            elif node.right is None :
                lt = node.left
                node = None
                return lt
            rightMinVal = self.minVal(node.right)
            node.value = rightMinVal
            node.right = self.delete(rightMinVal, node.right)
        if node is None :
            return node
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.balance(node)
        if balance > 1 and self.balance(node.left) >= 0 :
            return self.rotateR(node)
        if balance < -1 and self.balance(node.right) <= 0:
            return self.rotateL(node)
        if balance > 1 and self.balance(node.left) < 0:
            node.left = self.rotateL(node.left)
            return self.rotateR(node)
        if balance < -1 and self.balance(node.right) > 0  :
            node.right = self.rotateR(node.right)
            return self.rotateL(node)
        return node

Tree = AVL()
root = None
root = Tree.insert(3, root)
root = Tree.insert(5, root)
root = Tree.insert(7, root)
root = Tree.insert(1, root)
root = Tree.insert(2, root)
root = Tree.insert(4, root)
root = Tree.insert(6, root)
root = Tree.insert(7, root)
root = Tree.insert(8, root)
root = Tree.insert(9, root)
print("in Order : ")
Tree.inOrder(root)
root = Tree.delete(3, root)
print("in Order : ")
Tree.inOrder(root)
            
    
        