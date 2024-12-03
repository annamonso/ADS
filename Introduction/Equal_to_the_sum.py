

from yogi import scan

def check_sum(n, vector):
    res = False
    i=0 
    total_sum = sum(vector)
    # while res == False keep searching till you check all the values in the vector 
    while not res and i<n:
        x = vector[i]
        if x == (total_sum-x):
            res = True
        i +=1
            
            
    return res

if __name__ == '__main__':
    n = scan(int)
    while n is not None: 
        vector = [0]*n

        for k in range(n):
            num = scan(int)
            vector[k] = num
        
        res = check_sum(n,vector)
        
        if res:
            print('YES')
        else: 
            print('NO')
        
        n = scan(int)

