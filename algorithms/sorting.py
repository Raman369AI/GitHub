def bubblesort(list):
    length = len(list)-1
    # The pass
    for i in range(length):
        # The elements
        for j in range(length):
            if list[j]>list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
                print(list)
    return list

'''
Initial list: [29, 10, 14, 37, 13]
Pass 1: [10, 29, 14, 37, 13]
Pass 2: [10, 13, 14, 37, 29]
Pass 3: [10, 13, 14, 37, 29]
Pass 4: [10, 13, 14, 29, 37]
'''

def selectionsort(l):
        length = len(l)
        for i in range(length):
            smallest = i
            for k in range(i+1,length):
                if l[smallest] > l[k]:
                    smallest = k
            l[i],l[smallest] = l[smallest],l[i]
        return l


'''
Initial: [5,4,10,1,6,2]
Divide into two parts:
Sorted sublist and unsorted sublist
Take one variable from unsorted sublist and place it in sorted sublist at appropriate position.

'''

def insertionsort(list):
    length = len(list)
    #outer loop: seperating the sorted sub list
    for i in range(length):
        tmp = list[i]
        j = i -1
        while j >= 0 and tmp < list[j]:
            list[j+1] = list[j]
            j = j - 1
        l[j + 1] = tmp
    return list
             
    '''
    1. Find the smallest element in the list.
    2. Swap it with the first element.
    3.Find the next smallest element and swap it with the second element.
    4. Repeat this process, moving the boundary of the sorted and unsorted sections of the list until the entire list is sorted.
    '''
    
def mergesort(l):
    if len(l) == 1:
        return l
    mid = len(l)//2
    l_1 = l[:mid]
    l_2 = l[mid:]
    ll_1 = mergesort(l_1)
    ll_2 = mergesort(l_2)
    sorted_output = merge(ll_1,ll_2)
    return sorted_output

def merge(l1,l2):
    len_l1 = len(l1)
    len_l2 = len(l2)
    merged_list = []
    i = 0
    j = 0
    while i < len_l1 and j<len_l2:
        if l1[i] < l2[j]:
            merged_list.append(l1[i])
            i += 1
            print(merged_list)
        # even equal to condition is satisfied with else condition only.
        else:
            merged_list.append(l2[j])
            j += 1
            print(merged_list)
    end_l1 = l1[i:]
    end_l2 = l2[j:]
    return merged_list + end_l1 + end_l2

#time complexity is nlogn and space complexity is higher  - order n
# Additional space is as large as input itself.

#time complexity is nlogn
def quicksort(lst):
    length = len(lst)
    if length <= 1:
        return lst
    pivot = lst[-1]
    left = [x for x in lst if x < pivot]
    print(f'left:{left}')
    right = [x for x in lst if x > pivot]
    print(f'right:{right}')
    equal = [x for x in lst if x == pivot]
    print(f'equal:{equal}')

    return quicksort(left) + quicksort(equal) + quicksort(right)
    
    
    
l = [6,8,1,4,5,3,7,2]
print(quicksort(l))
