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

