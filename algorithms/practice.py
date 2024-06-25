'''
sorting algorithms
'''

sor = [3, 2, 5, 1, 0]

def bubblesort(lis):
    for i in range(len(lis)-1):
       for j in range(len(lis)-1):
        if lis[j]>lis[j+1] and j!=len(lis)-1:
            lis[j],lis[j+1] = lis[j+1],lis[j]
    return lis
print(bubblesort(sor))
        
