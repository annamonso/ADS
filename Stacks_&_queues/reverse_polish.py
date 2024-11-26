
from collections import deque
import sys


def reversepolish(tokens):
    s = deque()
    for k in tokens:
        if k == '+':
            b = s.pop() #we pop the second operand
            a = s.pop() #we pop the first operand
            s.append(a + b) #we add the result to the stack
        elif k == '-':
            b = s.pop()
            a = s.pop()
            s.append(a-b)
        elif k == '*':
            b = s.pop()
            a = s.pop()
            s.append(a*b)
        else: s.append(int(k)) #we add the integer to the stack
        
    return s.pop()


if __name__ == '__main__': 
     for line in sys.stdin:
          tokens = line.split()
          print(reversepolish(tokens))
        
