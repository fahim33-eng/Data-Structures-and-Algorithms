class BinarySearchTreeNode :
   def __init__(self, data) :
       self.data = data
       self.left = None
       self.right = None
   def addChild(self, data) :
       if data == self.data :
           return
       if data < self.data :
           if self.left :
               self.left.addChild(data)
           else :
               self.left = BinarySearchTreeNode(data)
       else :
           if self.right :
               self.right.addChild(data)
           else :
               self.right = BinarySearchTreeNode(data)
   def inOrderTraversal(self) :
       elements = []
       if self.left :
           elements += self.left.inOrderTraversal()
       elements.append(self.data)
       if self.right :
           elements += self.right.inOrderTraversal()
       return elements
   def search(self, value) :
       if value == self.data :
           return True
       elif value < self.data :
           if self.left :
               return self.left.search(value)
           else :
               return False
       else :
           if self.right :
               return self.right.search(value)
           else :
               return False
          
   def findMin(self) :
       if self.left is None :
           return self.data
       return self.left.findMin()
  
   def delete(self, val) :
       if val < self.data :
           if self.left :
               self.left = self.left.delete(val)
           else :
               return None
       elif val > self.data :
           if self.right :
               self.right = self.right.delete(val)
           else :
               return None
       else :
           if self.left is None and self.right is None :
               return None
           if self.left is None :
               return self.right
           if self.right is None :
               return self.left
           minVal = self.right.findMin()
           self.data = minVal
           self.right = self.right.delete(minVal)
       return self
      
  
bst = BinarySearchTreeNode(5)
bst.addChild(12)
bst.addChild(22)
bst.addChild(17)
bst.addChild(3)


print(bst.inOrderTraversal())


bst.delete(22)
print(bst.inOrderTraversal())