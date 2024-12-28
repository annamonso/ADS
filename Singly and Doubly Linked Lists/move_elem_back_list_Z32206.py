from yogi import scan 

class PositionalList:
    # Internal Node class
    class _Node:
        __slots__ = '_element', '_prev', '_next'
        
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    # Position class to represent the location of an element
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    # Internal utility methods
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise ValueError("p must be a valid Position")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._next is None:  # deprecated node
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    # PositionalList methods
    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, self._header, None)
        self._header._next = self._trailer
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def _insert_between(self, element, predecessor, successor):
        new_node = self._Node(element, predecessor, successor)
        predecessor._next = new_node
        successor._prev = new_node
        self._size += 1
        return self._make_position(new_node)

    def add_first(self, element):
        return self._insert_between(element, self._header, self._header._next)

    def add_last(self, element):
        return self._insert_between(element, self._trailer._prev, self._trailer)

    def add_before(self, p, element):
        node = self._validate(p)
        return self._insert_between(element, node._prev, node)

    def add_after(self, p, element):
        node = self._validate(p)
        return self._insert_between(element, node, node._next)

    def delete(self, p):
        node = self._validate(p)
        result = node._element
        node._prev._next = node._next
        node._next._prev = node._prev
        node._element = node._prev = node._next = None
        self._size -= 1
        return result

    def replace(self, p, element):
        node = self._validate(p)
        old_value = node._element
        node._element = element
        return old_value
    
    def move_to_back(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None: # convention for deprecated nodes
            raise ValueError('p is no longer valid')

        node = p._node
        e = node._element

        #Removing the node from its current position
        node._prev._next = node._next #the previous one is now linked to the one after node
        node._next._prev = node._prev #the next one is now linked to the one before node 

        # Insert the node at the back (before the trailer)
        predecessor = self._trailer._prev
        successor = self._trailer
        predecessor._next = node
        successor._prev = node 
        node._next = successor
        node._prev = predecessor

    def __str__(self):
        current = self._header._next
        
        elements = []
        backwards_elements = []
        while current != self._trailer:
            elements.append(str(current._element))  
            current = current._next  
        forward_str = ', '.join(elements)
        
        current = self._trailer._prev
        while current != self._header:
            backwards_elements.append(str(current._element))
            current = current._prev
        backward_str = ', '.join(backwards_elements)
        
        return f"{forward_str}\n{backward_str}"
            
if __name__ == '__main__':
  n = scan(int)
  t = PositionalList()
  for i in range(n):
    t.add_last(scan(int))
  i = scan(int)
  p = t.first()
  ## create the position and move it till the input value 
  for _ in range(i): p = t.after(p)
  print(f'list t:\n{t}')
  t.move_to_back(p)
  print(f'list after moving {i}-th element to back, t:\n{t}')

    
                
                
    
