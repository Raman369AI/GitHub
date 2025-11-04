'''
Given a descended sorted list determine the position of a card within shortest possible time
[0, 1, 2,3,.....n/2, ………..n-1]
Low <= high
Calculate mid = n/2
If the query is < n/2: low =0 and high = mid -1
Check for the first occurence and update the same
If the query is > n/2: low =mid + 1 and high = n - 1
If the query is = n/2: low = high = mid
'''
import sys

from logging_config import get_logger

logger = get_logger(__name__)

def binary_search(cards,query):
    length = len(cards)-1
    position = 0
    if  length == 0 or query == '':
            return -1
    while position <= length:
        middle = (length + position) // 2
        if query == cards[middle]:
           return middle
        elif query > cards[middle]:
            length = middle -1
        elif query < cards[middle]:
            position = middle + 1            
    return -1        

def locate_cards_first(cards,query):
    length = len(cards)-1
    position = 0
    result = -1
    if  length == 0 or query == '':
            return -1
    while position <= length:
        middle = (length + position) // 2
        if query == cards[middle]:
            result = middle 
            length = middle - 1
        elif query > cards[middle]:
            length = middle -1
        elif query < cards[middle]:
            position = middle + 1
    return result

def locate_cards_last(cards,query):
    length = len(cards)-1
    position = 0
    result = -1
    if  length == 0 or query == '':
            return -1
    while position <= length:
        middle = (length + position) // 2
        if query == cards[middle]:
            result = middle
            position = middle + 1
        elif query > cards[middle]:
            length = middle -1
        elif query < cards[middle]:
            position = middle + 1     
    return result       
           
        
'''
1. Check the cards length or if the query is empty then return a value of -1.
2. Check the edge cases if the query is present on the first or last of the list and return the position
3. Check the middle of the cards deck, if the query is less than go right else left 
and repeat the same until the position is found expecting a descending sorted list
'''
tests = []
test = {'input':{'cards':[11],'query':''},'output':0}
tests.append(test)
tests.append({'input':{'cards':[55, 54, 53, 52, 51, 50],'query':59},'output':1})
#tests.append({'input':{'cards':[55, 55, 54, 54, 52, 51],'query':54},'output':3})
#tests.append({'input':{'cards':[54, 54, 54, 54,53, 52, 51],'query':54},'output':3})
#tests.append({'input':{'cards':[54, 54, 54, 54,52, 52, 51],'query':51},'output':6})


''' test case for checking in  a coding round, using multiple cases to check the code'''
'''using ** allows python interpreter to take the dictionary keys as inputs of the function'''
with open('check.txt','a') as file:
    original_stdout = sys.stdout
    sys.stdout = file
    print('Binary Search')
    for i in range(len(tests)):
        print(f"cards: {tests[i]['input']['cards']}")
        print(f"query: {tests[i]['input']['query']}")
        #query_position = locate_cards(**tests[i]['input']) 
        query_position = binary_search(**tests[i]['input']) 

        if  query_position == tests[i]['output']:
            print(f"Test case passed and position is {query_position}")
        else:
            print(f"Test case for no cards or query - {query_position}")

