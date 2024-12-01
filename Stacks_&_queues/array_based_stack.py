import sys
from yogi import scan

class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class Full(Exception):
    """Error attempting to add an element to a full container"""
    pass

class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self, maxlen=0):
        """Create an empty stack with a maximum capacity."""
        self._data = [None] * maxlen  # Initialize with None
        self._maxlen = maxlen  # Store the maximum capacity
        self._size = 0  # Keep track of the current size

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0

    @staticmethod
    def _resize_check(previous, current):
        if previous != current:
            print(f'resized from {previous} to {current}')

    def push(self, e):
        """Add element e to the top of the stack."""
        previous = sys.getsizeof(self._data)
        if self._size >= self._maxlen:  # Check if the stack is full
            raise Full('Stack is full')
        self._data[self._size] = e  # Add the element at the next available position
        self._size += 1  # Increase the size
        current = sys.getsizeof(self._data)
        ArrayStack._resize_check(previous, current)

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[self._size - 1]  # Return the top element

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).
        
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        previous = sys.getsizeof(self._data)
        self._size -= 1  # Decrease the size first
        val = self._data[self._size]  # Get the top element
        self._data[self._size] = None  # Clear the reference (optional)
        current = sys.getsizeof(self._data)
        ArrayStack._resize_check(previous, current)
        return val

if __name__ == '__main__':
    n = scan(int)
    while n is not None:
        s = ArrayStack(n)  # Initialize stack with capacity
        print(f'len {len(s)}')
        if s.is_empty(): print('stack empty')
        
        # pushing elements
        for i in range(n + 1):
            try:
                s.push(i)
                print(f'{i} pushed')
            except Full:
                print('push error: stack full')
                
        # using accessors    
        print(f'len {len(s)}')
        try:
            print(f'top {s.top()}')
        except:
            print('top error: stack empty')

        # popping elements  
        for _ in range(n // 4):
            try:
                e = s.pop()
                print(f'{e} popped')
            except Empty:
                print('pop error: stack empty')

        # using accessors    
        print(f'len {len(s)}')
        try:
            print(f'top {s.top()}')
        except:
            print('top error: stack empty')

        # popping elements
        for _ in range(2 + 3 * (n // 4)):
            try:
                e = s.pop()
                print(f'{e} popped')
            except Empty:
                print('pop error: stack empty')

        print(f'len {len(s)}')
        try:  
            print(f'top {s.top()}')
        except Empty:
            print('top error: stack empty')

        print()
        
        n = scan(int)
