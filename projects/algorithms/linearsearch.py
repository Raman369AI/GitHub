import sys

from logging_config import get_logger

logger = get_logger(__name__)

def locate_cards(cards,query):
    position = 0
    length = len(cards)
    while True:
        if  length == 0 or query == '':
            return -1
        elif cards[0] == query:
                return 0
        elif cards[-1] == query:
                return (len(cards)-1)
        elif position == length - 1:
                return -1
        elif cards[position] == query :
            return position
        position += 1
            
                
            
            
            
'''
1. Check the cards length or if the query is empty then return a value of -1.
2. Check the edge cases if the query is present on the first or last of the list and return the position
3. Iterate over the length of the cards deck and return the position of the card if a match is 
found or increment the position and redo the step3 until a match is found
'''
tests = []
test = {'input':{'cards':[11],'query':''},'output':0}
tests.append(test)
tests.append({'input':{'cards':[11,13,14,14,15],'query':14},'output':2})
''' test case for checking in  a coding round, using multiple cases to check the code'''
'''using ** allows python interpreter to take the dictionary keys as inputs of the function'''
with open('check.txt','a') as file:
    original_stdout = sys.stdout
    sys.stdout = file
    print('Linear Search')
    for i in range(len(tests)):
        print(f"cards: {tests[i]['input']['cards']}")
        print(f"query: {tests[i]['input']['query']}")
        if locate_cards(**tests[i]['input']) == tests[i]['output']:
            print(f"Test case passed and position is {locate_cards(**tests[i]['input'])}")
            print(f"The position is {tests[i]['output']}")
        else:
            print("Test case for no cards or query - passed")
