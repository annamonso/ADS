from yogi import scan
import sys

class Empty(Exception):
  """Error attempting to access an element from an empty container"""
  pass


class LinkedQueue:
  """FIFO queue implementation using a singly linked list for storage."""


  #-------------------------- nested _Node class -------------
  class _Node:
    """Lightweight, nonpublic class for storing a singly linked node."""
    __slots__ = '_element', '_next'  

    
    def __init__(self, element, next):
      self._element = element
      self._next = next

      
  #------------------------------- queue methods -------------

  
  def __init__(self):
    """Create an empty queue."""
    self._head = None
    self._tail = None
    self._size = 0                   

    
  def __len__(self):
    """Return the number of elements in the queue."""
    return self._size

  
  def is_empty(self):
    """Return True if the queue is empty."""
    return self._size == 0

  
  def first(self):
    """Return (but do not remove) the element at the front of the queue. Raise Empty exception if the queue is empty. """
    if self.is_empty():
      raise Empty('Queue is empty')
    return self._head._element            

  
  def dequeue(self):
    """Remove and return the first element of the queue (i.e., FIFO). Raise Empty exception if the queue is empty."""
    if self.is_empty():
      raise Empty('Queue is empty')
    answer = self._head._element
    self._head = self._head._next
    self._size -= 1
    if self.is_empty():                   
      self._tail = None                   
    return answer

  
  def enqueue(self, e):
    """Add an element to the back of queue."""
    newest = self._Node(e, None)          
    if self.is_empty():
      self._head = newest                 
    else:
      self._tail._next = newest
    self._tail = newest                   
    self._size += 1

  def __str__(self):
    v = [None]*self._size
    n = self._head
    for i in range(self._size):
      v[i] = n._element
      n = n._next
    return ' '.join(str(e) for e in v)

  def merge(self, other):
      if self.is_empty():
        self._head = other._head
        self._tail = other._tail
        self._size = other._size
        other._head = other._tail = None
        other._size = 0
        
      else:
        n = self._head
        n1 = n._next
        n2 = other._head

        if not other.is_empty() and int(n2._element) < int(n._element):
            other._head = n2._next  
            n2._next = n            
            self._head = n2         
            n = self._head          
            n1 = n._next            
            n2 = other._head        
            self._size += 1
            other._size -= 1

        while not other.is_empty():
            if n2 is None:  
                break

            if n1 is None or int(n2._element) <= int(n1._element):
                temp = n2._next   
                n._next = n2      
                n2._next = n1     
                n = n2            
                n2 = temp         
                other._head = n2
                self._size += 1
                other._size -= 1
            else:
                n = n1
                n1 = n1._next
        other._head = None
        other._tail = None 
        other._size = 0


if __name__ == '__main__':
    q1 = LinkedQueue()
    q2 = LinkedQueue()
    i = 0 
    for line in sys.stdin:  
        values = line.strip().split()  
        for value in values:
            if i == 0:
              q1.enqueue(value)
            else:
              q2.enqueue(value)
        i += 1

    print(f'v[0]: {q1.__str__()}')
    print(f'v[1]: {q2.__str__()}')
    q1.merge(q2)
    print('After calling v[0].merge(v[1])')
    print(f'v[0]: {q1.__str__()}')
    print(f'v[1]: {q2.__str__()}')
    