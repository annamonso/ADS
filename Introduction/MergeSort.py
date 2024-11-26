def merge(v, p, q, r):
    L = v[p:q+1]
    R = v[q+1:r+1]

    i=0 #i indexes the smallest remaining element in L
    j=0 #j indexes the smallest remaining element in R
    k=p
    while i<len(L) and j<len(R):
        if L[i]<=R[j]:
            v[k] = L[i]  
            i +=1
        else :
            v[k] = R[j]
            j += 1
        k +=1
        #After the while loop either all of L or all of R has been copied back
        #If it terminates because all of R has been copied, then j=len(R) but i<len(L) -> not all L has been copied back
        #Thus, we require another loop to copy the remaining values of L into the last positions of v

    while i<len(L):
        v[k] = L[i]
        i += 1
        k += 1
    while j<len(R):
        v[k] = R[j]
        j += 1
        k +=1
    return v


def mergesort_rec(v, p, r):
    if p>=r: return v #the array only contains one element. It is trivially sorted
    if p<r: 
        q = (p+r)//2
        mergesort_rec(v,p,q)
        mergesort_rec(v,q+1,r)
        merge(v,p,q,r)  

def mergesort(v): 
  mergesort_rec(v, 0, len(v)-1)