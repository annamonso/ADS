from yogi import scan



class BinTree:
  #------------------- nested _Node class ---------------------
  class _Node:
    __slots__ = '_element', '_left', '_right'  

    def __init__(self, element, left=None, right=None):
      self._element = element  
      self._left  = left
      self._right  = right

      
  #------------------- public methods --------------------
  # Constructor
  def __init__(self, *rest):
    n = len(rest) # rest is the list of arguments 
    if n == 0:      
      self._root = None
    elif n == 1:   
      self._root = rest[0]
    else:          
      self._root = self._Node(rest[0], rest[1]._root, rest[2]._root)


  # Checks whether the tree is empty.
  def is_empty(self):
    return self._root == None

  # Returns the element stored in the root node    
  def root_element(self):
    return self._root._element    

  # Returns the left subtree 
  def left_subtree(self):
    return BinTree(self._root._left)

  # Returns the right subtree 
  def right_subtree(self):
    return BinTree(self._root._right)
         

# Prints a binary tree in in-order with the right subtree processed
# in first place, then the root node, and finally the left subtree.
def printInorder_draw(t, depth=0):
  if not t.is_empty(): 

     printInorder_draw(t.right_subtree(), depth+1)
     
     print(' '*2*depth, end='')
     print(t.root_element())

     printInorder_draw(t.left_subtree(), depth+1)

     
        

# Reads a binary tree in pre-order (empty trees are represented as -1).    
def readBinTree():
  def buildTree():
      value = scan(int)  
      if value == -1:    
          return None
      
      node = BinTree._Node(value)
      # Recursively read left and right subtrees
      node._left = buildTree()
      node._right = buildTree()
      return node

  t = BinTree()
  t._root = buildTree()  # Start building from the root
  return t

# Pre: t is a BST of integer numbers
# Post: If n is in t, the result is True; otherwise, the result is False.  
def search(t, n):
    if t is None or t.is_empty():
        return False
    if t._root._element == n:
        return True
    # Recursively search in the left and right subtrees
    left_subtree = BinTree(t._root._left) if t._root._left else None
    right_subtree = BinTree(t._root._right) if t._root._right else None
    return search(left_subtree, n) or search(right_subtree, n)

      
     
if __name__ == '__main__': 
    t = readBinTree()
    # printInorder_draw(t)
    n = scan(int)
    while n is not None:
      if search(t, n):
        print(n, 1)
      else:
        print(n, 0)
      n = scan(int)
      



    
