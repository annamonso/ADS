

def insertion_sort(v):
    for i in range(1, len(v)):
        num = v[i]
        j = i - 1
        # Ho compara amb el ultim i si es mes gran ja esta be 
        # En el cas que sigui mes petit que el ultim processat va comprovant fins que troba un mes petit o arriba al principi amb el cas de j-1 
        while j >= 0 and v[j] > num:
            # va movent els numeros mes grans cap a la dreta
            v[j + 1] = v[j]
            j -= 1
        v[j + 1] = num

    
    return v      
            



if __name__ == '__main__':
    v = [5.0, 2.0, 9.0, 1.0, 7.0]
    res = insertion_sort(v)
    print(res)

        