from yogi import scan

"""
Pre: v is an array of integer numbers. s is sum(v).
Post: if len(v) = 0 or there is an index 0 <= i < len(v) such that 
sum(v) - v[i] = v[i], the result is true; otherwise, the result is false.
"""
def sum_of_the_rest(v, s):
    i = 0
    found = False
    """
    Invariant: INSERT YOUR ANSWER 
    """
    while not found and i < len(v):
        if v[i] == s - v[i]: found = True
        else: i = i+1
    return found or len(v) == 0


"""
Justify the correctness and termination of function sum_of_the_rest. 
"""


if __name__ == '__main__':
    n = scan(int)
    while n is not None: 
        v = [0]*n
        sum = 0
        for j in range(n):
            v[j] = scan(int)
            sum += v[j]
        if sum_of_the_rest(v,sum): print("YES")
        else: print("NO")
        n = scan(int)
