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

     
        

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Reads a binary tree in pre-order (empty trees are represented as -1).
    def readBinTree():
        def helper(values):
            value = next(values)  # Lee el siguiente valor
            if value == -1:
                return None  # Nodo vacío
            node = TreeNode(value)  # Crea el nodo con el valor actual
            node.left = helper(values)  # Construye el subárbol izquierdo
            node.right = helper(values)  # Construye el subárbol derecho
            return node

        # Leer los valores desde la entrada estándar
        values = map(int, input("Enter the tree in pre-order: ").split())
        return helper(iter(values))

    # Pre: t is a BST of integer numbers
    # Post: If n is in t, the result is True; otherwise, the result is False.  
    def search(t, n):
        current = t
        while current is not None:
            if n == current.value:
                return True  # Se encontró el valor
            elif n < current.value:
                current = current.left  # Buscar en el subárbol izquierdo
            else:
                current = current.right  # Buscar en el subárbol derecho
        return False  # No se encontró el valor

     
 if __name__ == "__main__":
    # Leer toda la entrada
    import sys
    input_data = sys.stdin.read().strip().split("\n")
    
    # La primera línea contiene los valores del árbol en preorden
    tree_values = list(map(int, input_data[0].split()))
    
    # El resto son los números que queremos buscar
    search_values = list(map(int, input_data[1:]))
    
    # Construir el árbol binario
    def helper(values):
        value = next(values)  # Lee el siguiente valor
        if value == -1:
            return None  # Nodo vacío
        node = TreeNode(value)  # Crea el nodo con el valor actual
        node.left = helper(values)  # Construye el subárbol izquierdo
        node.right = helper(values)  # Construye el subárbol derecho
        return node

    tree = helper(iter(tree_values))

    # Buscar cada valor en el árbol
    results = []
    for value in search_values:
        results.append(f"{value}: {search(tree, value)}")
    
    # Imprimir los resultados
    print("\n".join(results))

    
