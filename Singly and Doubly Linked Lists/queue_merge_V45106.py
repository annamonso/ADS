import sys
from yogi import scan


class Empty(Exception):
  """Error attempting to access an element from an empty container"""
  pass


class LinkedQueue:
  """FIFO queue implementation using a singly linked list for storage."""


  #-------------------------- nested _Node class -------------
  class _Node:
    """Lightweight, nonpublic class for storing a singly linked node."""
    __slots__ = '_element', '_next'  # streamline memory usage

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


  def __iter__(self):
    n = self._head
    while n is not None:
      yield n._element
      n = n._next
      

  def __str__(self):
    ''' Print the elements in the queue separated by a white space. 
    '''
    # IMPLEMENT __str__ WITHOUT USING ANY PUBLIC METHOD OF LinkedQueue
    ##########
    return ' '.join(str(e) for e in self)
    

  def merge(self, other):
    ''' Merge queues 'self' and 'other' as follows. If 'self' is e_1, e_2, ..., e_n 
    and 'other' is o_1, o_2, ..., o_m, after executing self.merge(other) the 
    queue 'self' contains the sequence e_1,o_1,e_2,o_2,...e_n,o_n,o_n+1,...,o_m if 
    n <= m, and the sequence e_1,o_1,e_2,o_2,...e_m,o_m,e_m+1,...,e_n if 
    n > m, and in both cases the queue other is empty.  
    '''
    # IMPLEMENT merge WITHOUT USING ANY PUBLIC METHOD OF LinkedQueue
    ##########
    if len(other) == 0: return
    if len(self) == 0:
      self._head = other._head
      self._tail = other._tail
    else:  # both linked lists are non-empty  
        n1 = self._head # to traverse self's linked list
        n2 = other._head # to traverse other's linked list
        self_turn = False # self_turn is True if the next node to add to the linked list result
                          # belongs to self; otherwise, the next node to add to the linked list
                          # result belongs to other.
        n = n1 # last node of the linked list result (which must be assigned to self eventually)
        n1 = n1._next
        while n1 is not None and n2 is not None:
           if self_turn:
              n._next = n1
              n1 = n1._next
           else:
              n._next = n2
              n2 = n2._next
           n = n._next  
           self_turn = not self_turn # switch turn

        if n2 is None: # len(other) < len(self)
          n._next = n1
    
        if n1 is None: # len(self) <= len(other)
          n._next = n2
          self._tail = other._tail
          
    self._size += other._size      
    other._size = 0
    other. _head = None
    other._tail = None
      
    


if __name__ == '__main__':
  v = [LinkedQueue() for _ in range(2)]
  i = 0
  for line in sys.stdin:
    tokens = line.split()
    for e in tokens:
      v[i].enqueue(int(e))
    i += 1

  print(f'v[0]: {v[0]}')
  print(f'v[1]: {v[1]}')  
  v[0].merge(v[1])
  print('After calling v[0].merge(v[1])')
  print(f'v[0]: {v[0]}')
  print(f'v[1]: {v[1]}')  
  
    



