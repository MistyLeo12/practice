class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.v = key

class Tree:
    def __init__(self):
        self.root = None
    
    def getRoot(self):
        return self.root
    
    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)
    def _add(self, val, node):
        if(val < node.v):
            if(node.left is not None):
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if(node.right is not None):
                self._add(val, node.right)
            else:
                node.right = Node(val)
    def find(self, val):
        if(self.root is not None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.v):
            return node
        elif(val < node.v and node.left is not None ):
            self._find(val, node.left)
        elif(val > node.v and node.right is not None ):
            self._find(val, node.right)
    def deleteTree(self):
        self.root = None
    
    def printTree(self):
        if(self.root is not None):
            self._printTree(self.root)
        
    def _printTree(self, node):
        if(node != None):
            self._printTree(node.left)
            print (str(node.v) + '')
            self._printTree(node.right)
    

tree = Tree()
tree.add(3)
tree.add(9)
tree.add(4)
tree.add(11)
tree.add(2)
tree.add(33)
tree.printTree()
print(tree.find(4))
print (tree.find(10))
tree.deleteTree()
tree.printTree()

test_array = [1,11, 77, 9, 8, 10, 666, 12, 23, 2]
