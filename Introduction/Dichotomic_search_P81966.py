''' 
    recursive function that returns the position of x in the subvector v[left..right]. 
    The function must return -1 if x does not belong to v[left..right] or if left > right
'''

# keeps dividing the array till the mid == value, then returns mid positon
def position(x, v, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2

    if v[mid] == x:
        return mid

    elif v[mid] > x:
        return position(x, v, left, mid - 1)

    else:
        return position(x, v, mid + 1, right)

