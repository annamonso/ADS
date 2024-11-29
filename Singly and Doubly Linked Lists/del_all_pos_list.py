import sys
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
                

    def delete_all(self, value):
        node = self._header._next  
        while node is not None:
            if node._element == value:
                #print(f"Eliminando valor {value}")
                if node == self._header._next:  
                    self._header._next = node._next
                    if node._next is not None:  
                        node._next._prev = self._header
                elif node._next is None:  
                    self._tail = node._prev
                    node._prev._next = None
                else:  
                    node._prev._next = node._next
                    node._next._prev = node._prev
                self._size -= 1 
                #print(f"Lista después de eliminar {value}: {self.__str__()}")
            node = node._next  
       
        
    def __str__(self):
        forward_list = []
        node = self._header._next  
        while node is not None:
            forward_list.append(str(node._element))
            node = node._next
        forward_str = ', '.join(forward_list)
        backward_list = []
        node = self._trailer  
        while node is not None and node != self._header:
            backward_list.append(str(node._element))
            node = node._prev
        backward_str = ', '.join(backward_list)
        return f"{forward_str}\n{backward_str}"
    
if __name__ == '__main__':
    q1 = PositionalList()
    n = scan(int)
    for i in range(n):  
        value = scan(int)
        if i == 0:
            q1.add_first(value)
        else:
            q1.add_last(value)
        #print(f"q1 after adding value {value}: {q1.__str__()}")

    value = scan(int)
    res = q1.__str__()
    print("list t:")
    print(res)
    q1.delete_all(value)
    print("list after deletion t:")
    res = q1.__str__()
    print(res)
