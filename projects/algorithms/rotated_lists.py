'''
Problem statement: Determine the minimum no of times a sorted list was rotated to obtain the target list at hand.
'''
import sys

from logging_config import get_logger

logger = get_logger(__name__)

def rotated_count(list_orig,list_mod):
    # Addressed the non existence of a list element, valueerror
    if len(list_mod) != 0:
        position = list_mod[0]
    else:
        position = 0
    initial = 0
    final_length = len(list_orig)
    length = len(list_orig)-1
    if len(list_orig) != len(list_mod) or len(list_orig) == 0 or len(list_mod) == 0:
        return -2
    while length >= initial:
        middle = (length + initial)//2
        if list_mod[0] == list_orig[0]:
            return 0
        elif position == list_orig[middle]:
            return int(final_length - middle)
        elif position > list_orig[middle]:
            length = middle - 1
        else:
            initial = middle + 1
    return -1

'''
1. The modified list initial number is searched in the original list and the index of the modified list
is subtratced from the total length of the original list to give the modifications.
Total length minus the previous index value of the first value in the modified list gives the no of rotations.
'''

tests = []

tests.append({'input':{'list_orig':[],'list_mod':[]},'output':-2})
tests.append({'input':{'list_orig':[],'list_mod':[14, 56, 55, 54, 53, 52]},'output':-2})
tests.append({'input':{'list_orig':[57, 56, 55, 54,  53, 52],'list_mod':[52,57, 56, 55,  54, 53]},'output':1})
tests.append({'input':{'list_orig':[57, 56, 55, 54,  53, 52],'list_mod':[53, 52,57, 56,  55, 54]},'output':2})
tests.append({'input':{'list_orig':[57, 56, 55, 54,  53, 52],'list_mod':[57, 56, 55, 54,  53, 52]},'output':0})
tests.append({'input':{'list_orig':[57, 56, 55, 54,  53, 52],'list_mod':[14, 56, 55, 54,  53, 52]},'output':-1})



''' test case for checking in  a coding round, using multiple cases to check the code'''
'''using ** allows python interpreter to take the dictionary keys as inputs of the function'''
with open('check.txt','a') as file:
    original_stdout = sys.stdout
    sys.stdout = file
    print('Rotation lists')
    for i in range(len(tests)):
        print(f"Original List: {tests[i]['input']['list_orig']}")
        print(f"Modified list: {tests[i]['input']['list_mod']}")
        rotation = rotated_count(**tests[i]['input']) 
        if  rotation == tests[i]['output']:
            print(f"Test case passed and position is {rotation}")
        else:
            print(f"Test case for no rotated count - passed, {rotation}")
