'''
sorting algorithms
'''

sor = [3, 2, 5, 1, 0]

def bubblesort(lis):
    h = 0
    #for i in range(len(lis)-1):
    for j in range(len(lis)-1):
        if lis[j]>lis[j+1] and j!=len(lis)-1:
            lis[j],lis[j+1] = lis[j+1],lis[j]
            bubblesort(lis)
            h = h+1
            print(h)
    return lis
print(bubblesort(sor))


'''
1. Append the first element
2. Check with the minimum element and last element and push
'''

        
