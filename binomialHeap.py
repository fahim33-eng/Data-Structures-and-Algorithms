class BinomialTree:
    def __init__(self, val):
        self.val = val
        self.children = []
        self.order = 0
 
    def addAtTheEnd(self, tree):
        self.children.append(tree)
        self.order = self.order + 1
 
 
class BinomialHeap:
    def __init__(self):
        self.trees = []
 
    def extract_min(self):
        if self.trees == []:
            return None
        smallest_node = self.trees[0]
        for tree in self.trees:
            if tree.val < smallest_node.val:
                smallest_node = tree
        self.trees.remove(smallest_node)
        h = BinomialHeap()
        h.trees = smallest_node.children
        self.merge(h)
 
        return smallest_node.val
 
    def getMin(self):
        if self.trees == []:
            return None
        least = self.trees[0].val
        for tree in self.trees:
            if tree.val < least:
                least = tree.val
        return least
 
    def combineRoots(self, h):
        self.trees.extend(h.trees)
        self.trees.sort( key = lambda tree : tree.order )
 
    def merge(self, h):
        self.combineRoots(h)
        if self.trees == []:
            return
        i = 0
        while i < len(self.trees) - 1:
            current = self.trees[i]
            after = self.trees[i + 1]
            if current.order == after.order:
                if (i + 1 < len(self.trees) - 1 and self.trees[i + 2].order == after.order):
                    after_after = self.trees[i + 2]
                    if after.val < after_after.val:
                        after.addAtTheEnd(after_after)
                        del self.trees[i + 2]
                    else:
                        after_after.addAtTheEnd(after)
                        del self.trees[i + 1]
                else:
                    if current.val < after.val:
                        current.addAtTheEnd(after)
                        del self.trees[i + 1]
                    else:
                        after.addAtTheEnd(current)
                        del self.trees[i]
            i = i + 1
 
    def insert(self, val):
        newHeap = BinomialHeap()
        newHeap.trees.append(BinomialTree(val))
        self.merge(newHeap)
 
 
binomialHeap = BinomialHeap()

binomialHeap.insert(15)
binomialHeap.insert(51)
binomialHeap.insert(13)
binomialHeap.insert(25)

print(binomialHeap.getMin())