import sys          
from collections import deque

def check_parentesis(word):
    stack = deque()
    
    pairs = {')': '(', ']': '['}
    check = True

    for c in word: 
        if c == '[' or c == '(':  
            stack.append(c)
        elif c == ']' or c == ')':  
            if not stack or stack.pop() != pairs[c]: 
                check = False 
    
    if stack: 
        check = False 
    
    if check:
        print(f"{word} is correct")
    else:
        print(f"{word} is incorrect")


if __name__ == '__main__': 
    input_data = sys.stdin.read().strip() 
    tokens = input_data.split()  
    for token in tokens: 
        check_parentesis(token)  
