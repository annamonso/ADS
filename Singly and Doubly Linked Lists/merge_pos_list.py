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
    
    def merge(self, other):
        if self.is_empty():
            # si el self esta buit poses que señali a l'altre cua 
            self._header = other._header
            self._trailer = other._trailer
            self._size = other._size
            other._header = other._trailer = None
            other._size = 0
            return

        if other.is_empty():
            # No fas res
            return  

        n1 = self._header._next  
        n2 = other._header._next 
        
        # Merge dels dos primers elements per gestionar el header
        if n2._element < n1._element:
            # Move the first element of `other` to the front of `self`
            self._header._next = n2
            n2._prev = self._header
            other._header._next = n2._next
            if n2._next is not None:
                n2._next._prev = other._header
            n2._next = n1
            n1._prev = n2
            self._header = n2 
            other._size -= 1
            self._size += 1
            
        # Merge de la resta de la queue
        while n2._element is not None:
            if n1._element is None or n2._element <= n1._element:
                # Inserta el nodo `n2` antes de `n1` en `self`
                temp = n2._next
                if n2._prev:
                    n2._prev._next = n2._next
                if n2._next:
                    n2._next._prev = n2._prev

                    n2._next = n1
                if n1 is not None:
                    n2._prev = n1._prev
                    if n1._prev:
                        n1._prev._next = n2
                    n1._prev = n2
                else:
                    # Si `n1` es `None`, inserta al final
                    self._trailer._prev._next = n2
                    n2._prev = self._trailer._prev
                    self._trailer._prev = n2
                    n2._next = self._trailer

                n2 = temp  # Avanza al siguiente nodo de `other`
                self._size += 1
                other._size -= 1
            else:
                n1 = n1._next  # Avanza al siguiente nodo de `self`


        # If `n2` has remaining elements, append them to the end of self
        if n2._element is not None and n1._element is None:
            self._trailer._next = n2
            n2._prev = self._trailer
            self._trailer = other._trailer
            self._size += other._size
            other._header = other._trailer = None
            other._size = 0

        
    
    def __str__(self):
        if self._size == 0:
            return ""
        current = self._header._next
        elements = []
        while current != self._trailer:
            elements.append(str(current._element))  
            current = current._next  
        forward_str = '  '.join(elements)

        return f"{forward_str}"
            
if __name__ == '__main__':
    q1 = PositionalList()
    q2 = PositionalList()
    n = scan(int)
    for i in range(n):  
        value = scan(float)
        if i == 0:
            q1.add_first(value)
        else:
            q1.add_last(value)
    n = scan(int)
    for i in range(n):  
        value = scan(float)
        if i == 0:
            q2.add_first(value)
        else:
            q2.add_last(value)
            

    q1.merge(q2)
    
    print(f"t1  {q1.__str__()}")
    print(f"t2", end="")


