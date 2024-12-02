from yogi import scan


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

      
  # Returns the maximum value of a non-empty tree
  # def maxim(self):
      # COMPLETE THE CODE


    
  def __str__(self):
    if self._root is None:
      return ''
    els = []
    self._node_str(self._root, els)
    return ' '.join(els)

  
  #---------------- non-public methods ------------------------

  
  # returns a reference to node with maximum value
  # def _maxim(self, node):
     # COMPLETE THE CODE


    
  def _node_str(self, node, elements):
    elements.append(str(node._element))
    for child in node._children:
      self._node_str(child, elements)
      
    
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
def printPreordre(t, depth=0):
  if not t.is_empty(): 
     print(' '*2*depth, end='')
     print(t.root_element())
     for st in t.subtrees():
          printPreordre(st, depth+1)

def maxim(t):
    max_value = 0 
    if t._root is None:
        return max_value
    def find_max(node):
        if node is None:
            return max_value
        max_value = node._element
        n = node._children 
        for i in range(len(n)):
            max_value = max(max_value, find_max(n[i]))
        return max_value
    return find_max(t._root)

    # elem = t._root._element
    # if (elem > max):
    #     max = elem
    # n = t._root._children
    # for i in range(len(n)):
    #     leaf = n[i]
    #     if(leaf._element > max):
    #         max = leaf._element
    #     leaf_childrens = leaf._children
    #     for i in range(len(leaf_childrens)):
    #         leaf2 = n[i]
    #         if(leaf2._element > max):
    #             max = leaf2._element
    # return max 
         
if __name__ == '__main__':
    t = readTree()
   # print('\nPre-order traversal\n')
   # printPreorder(t)
    print(f"{maxim(t)}")