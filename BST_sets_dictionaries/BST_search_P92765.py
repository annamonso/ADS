from yogi import scan


class Empty(Exception):
  """Error attempting to access an element from an empty container"""
  pass


class BST_OrdSet:

  #----- nested _Node class ------------------

  class _Node: 
    __slots__ = '_element', '_left', '_right'   

    def __init__(self, ele, le=None, ri=None):
      self._element = ele
      self._left    = le
      self._right   = ri


  #---------Ordered Set public methods -------
  
  def __init__(self):
    self._root = None
    self._size = 0


  # Return True if the set is empty.
  def is_empty(self):
    return self._root is None

  
  # Return the number of elements in the set.
  def __len__(self):
    return self._size
  
  # Returns True if the set contains element x
  def search(self, x):
    return self._search(self._root, x)

  
  # Find the smallest element in a non-empty set.
  def findMin(self):
    if self.is_empty():
      raise Empty('Set is empty')
    return self._findMin(self._root)._element

  
  # Find the largest element in a non-empty set.  
  def findMax(self):
    if self.is_empty():
      raise Empty('Set is empty')
    return self._findMax(self._root)._element
  
  # Insert element x, if it was not in the set. 
  def insert(self, x):
    if self.is_empty():
      self._root = BST_OrdSet._Node(x)
      self._size += 1
    else:
      self._insert(self._root, x)

      
  # Remove element x from the set.
  def remove(self, x):
    self._remove(self._root, x)

    
  # Generate an iteration of all elements in the set in ascending order.  
  def __iter__(self):
    yield from self._inorder(self._root)


    
  #----BST based Ordered Set private methods -------

  
  # Search x in subtree rooted at 'node'. 
  def _search(self, node, x):
    if node is None: # empty subtree
      return False
    if x < node._element:
      return self._search(node._left, x)
    elif node._element < x:
      return self._search(node._right, x)
    return True # node's element is equal to x

  
  # Returns a reference to the node containing the
  # smallest element in the subtree rooted at node.
  def _findMin(self, node):
    if node._left is None:
      return node
    return self._findMin(node._left)

  
  # Returns a reference to the node containing the
  # largest element in the subtree rooted at node.
  def _findMax(self, node): 
    while node._right is not None: 
      node = node._right # iterative implementation
    return node

  
  # Insert x in subtree rooted at 'node'.  
  def _insert(self, node, x, pa=None, leftC=False):
    if node is None: # pa is node's parent
      if leftC: # node is left child of pa 
        pa._left = BST_OrdSet._Node(x)
      else:     # node is rigth child of pa 
        pa._right = BST_OrdSet._Node(x)
      self._size += 1
    elif x < node._element:   
      self._insert(node._left, x, node, True)
    elif node._element < x:
      self._insert(node._right, x, node, False)

      
  # Remove x from subtree rooted at 'node'.
  def _remove(self, node, x):
   if node is None: return # x is not in the set
   if x < node._element:
    self._remove(node._left, x)
   elif node._element < x:
    self._remove(node._right, x)
   else: # x is equal to node._element
    self._size -= 1
    if node._left is not None and\
       node._right is not None:
       # node has two children
       m = self._findMin(node._right)
       node._element = m._element
       self._remove(node._right,m._element,node,False)
       # x is equal to node._element
       # node has at most one child
       # node's left child is not empty 
    elif node._left is not None:
       node = node._left
    else: # node's left child is empty
           # node's right child might be empty
       node = node._right

      
  def _inorder(self, nod):
    if nod is not None: 
      yield from self._inorder(nod._left)
      yield nod._element
      yield from self._inorder(nod._right)    
        
    
  # Prints a binary tree in pre-order
  def printPreOrder(self):
    self._printPreOrder(self._root)

  def _printPreOrder(self, node):
    if node is not None: 
     print(f'{node._element}', end='\n')
     self._printPreOrder(node._left)
     self._printPreOrder(node._right)
     
  # def search(self, value):
  #   if value == self._element:
  #       return True  # value found
  #   if value < self._element:
  #       if self._left is None:
  #           return False  # value not part of the tree
  #       return self._left.search(value)
  #   else:
  #       if self._right is None:
  #           return False  # value not part of the tree
  #       return self._right.search(value)


   
def readBinTree():
    def buildTree():
        value = scan(int)
        if value == -1:
            return None
        
        node = BST_OrdSet._Node(value)
        node._left = buildTree()
        node._right = buildTree()
        return node

    t = BST_OrdSet()
    t._root = buildTree()  # Start building from the root
    return t

if __name__ == '__main__':
    n = scan(int)  # Leer y descartar el primer número (número de elementos)
    t = readBinTree()  # Crear el árbol con los valores de entrada

    # Procesar las consultas
    while True:
        query = scan(int)
        if query is None:
            break
        found = t.search(query)
        print(query, 1 if found else 0)
    
