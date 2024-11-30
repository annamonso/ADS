from yogi import scan
from collections import deque

class Tree:
  #------------------- nested _Node class ---------------------
  class _Node:
    __slots__ = '_element', '_children'  

    def __init__(self, element, children=[]):
      self._element = element  
      self._children  = children  


  #------------------- public methods --------------------
  # Constructor
  def __init__(self, *rest):
    n = len(rest) # rest is the list of arguments 
    if n == 0:      # rest is the empty list
        self._root = None
    elif n == 1:   # rest is a list containing a single node
        self._root = rest[0]
    else:            # rest is a list containing the root element
                     # and a possibly empty list of subtrees
        children = []
        for i in range(len(rest[1])):
            children.append(rest[1][i]._root)
        self._root = self._Node(rest[0], children)


  # Checks whether the tree is empty.
  def is_empty(self):
    return self._root == None

  # Returns the element stored in the root node    
  def root_element(self):
    return self._root._element    

  # Returns the list of subtrees 
  def subtrees(self):
    for child in self._root._children:
      yield Tree(child) 


# Reads a tree     
def readTree():
  element = scan(int)
  if element is None:
    return Tree()
  n = scan(int)
  subtrees = [None]*n
  for i in range(n):
      subtrees[i] = readTree()
  return Tree(element, subtrees)



# Prints a tree in pre-order
def printPreorder(t, depth=0):
  if not t.is_empty(): 
     print(' '*2*depth, end='')
     print(t.root_element())
     for st in t.subtrees():
          printPreorder(st, depth+1)
          

def maxim(t):
    max = 0 
    return max 
         
if __name__ == '__main__':
    t = readTree()
    print('\nPre-order traversal\n')
    printPreorder(t)
    
