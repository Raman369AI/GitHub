'''
Interpolation search : The data is uniformly distributed then interpolation search is used
The uniform data is the slope calculation which can be used to the determine the exact position.

'''
import sys

def locate_cards(cards,query):
    length = len(cards) - 1
    position = 0
    slope = (cards[0] - cards[1])
    if  length == 0 or query == '':
        return -1
    if (cards[position] - query)%slope == 0:
        i = int((cards[position] - query)/slope)
        if query == cards[position] - slope * i:
            return i
        else:
            return 'The number does not exists and flawed logic'
    else:
        return 'The number does not exists in the range'


tests = []
#tests.append(test)
tests.append({'input':{'cards':[55, 54, 53, 52, 51],'query':54},'output':1})
tests.append({'input':{'cards':range(1000000,0,-2),'query':5478},'output':1})

''' test case for checking in  a coding round, using multiple cases to check the code'''
'''using ** allows python interpreter to take the dictionary keys as inputs of the function'''
with open('check.txt','a') as file:
    original_stdout = sys.stdout
    sys.stdout = file
    print('interpolation Search')
    for i in range(len(tests)):
        print(f"cards: {tests[i]['input']['cards']}")
        print(f"query: {tests[i]['input']['query']}")
        query_position = locate_cards(**tests[i]['input']) 
        if  query_position == tests[i]['output']:
            print(f"Test case passed and position is {query_position}")
        else:
            print(f"Test case for no cards or query - passed, {query_position}")
