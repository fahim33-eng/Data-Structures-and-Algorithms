from heapq import heappush, heappop

class node :
    def __init__(self, freq, symbol, left = None, right = None) :
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''
    
    def __lt__(self, other) :
        return self.freq < other.freq
    
def printNodes(node, val = '') :
    newVal = val + str(node.huff)
    if node.left :
        printNodes(node.left, newVal)
    if node.right :
        printNodes(node.right, newVal)
    if not node.left and not node.right :
        print(f"{node.symbol} -> {newVal}")

characters = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [15, 13, 22, 3, 30, 10]

nodes = []

for x in range(len(characters)) :
    heappush(nodes, node(freq[x], characters[x]))

while len(nodes) > 1 :
    left = heappop(nodes)
    right = heappop(nodes)
    left.huff = 0
    right.huff = 1
    newNode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    heappush(nodes, newNode)
printNodes(nodes[0])
