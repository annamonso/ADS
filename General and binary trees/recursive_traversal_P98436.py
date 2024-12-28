from yogi import scan
import sys

class BinTree:
    class _Node:
        __slots__ = '_element', '_left', '_right'

        def __init__(self, element, left=None, right=None):
            self._element = element
            self._left = left
            self._right = right

    def __init__(self, *rest):
        n = len(rest)
        if n == 0:
            self._root = None
        elif n == 1:
            self._root = rest[0]
        else:
            self._root = self._Node(rest[0], rest[1]._root, rest[2]._root)

    def is_empty(self):
        return self._root is None

    def root_element(self):
        return self._root._element

    def left_subtree(self):
        return BinTree(self._root._left)

    def right_subtree(self):
        return BinTree(self._root._right)


    #Postorder traversal
    #work at the root node is performed after the subtrees 
    #have been processed in postorder
    def postorder(self):
        def _postorder(node):
            if node is None:
                return []
            left = _postorder(node._left)
            right = _postorder(node._right)
            return left + right + [node._element]

        return _postorder(self._root)
    
    #Inorder traversal
    #1st process left subtree in inorder, then the root and
    #the right subtree in inorder
    def inorder(self):
        def _inorder(node):
            if node is None:
                return []
            left = _inorder(node._left)
            right = _inorder(node._right)
            return left + [node._element] + right
        
        return _inorder(self._root)



def readBinTree():
    element = scan(int)
    if element == -1:
        return BinTree()
    left = readBinTree()
    right = readBinTree()
    return BinTree(element, left, right)


if __name__ == '__main__':
    t = readBinTree()
    pos = t.postorder()  
    # If the tree is empty, print "pos:" without spaces
    if len(pos) == 0: print("pos:")
    else: print("pos:", " ".join(map(str, pos)))
    ino = t.inorder()
    # If the tree is empty, print "ino:" without spaces
    if len(pos) == 0: print("ino:")
    else: print("ino:", " ".join(map(str, ino)))
