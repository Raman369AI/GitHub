'''
Given a sorted list determine the position of a card within shortest possible time
'''

def locate_cards(cards,query):
    position = 0
    length = len(cards)-1
   
    while position < length:
        middle = (length + position) // 2
        if  length == 0 or query == '':
            return -1
        elif cards[0] == query:
            return 0
        elif cards[-1] == query:
            return (len(cards)-1)
        elif query == cards[middle]:
            return middle
        elif query > cards[middle]:
            length = middle -1
        elif query < cards[middle]:
            position = middle+1
    return -1         
                
            
            
            
'''
1. Check the cards length or if the query is empty then return a value of -1.
2. Check the edge cases if the query is present on the first or last of the list and return the position
3. Check the middle of the cards deck, if the query is less than go right else left and repeat the same until the position is found
'''
tests = []
#test = {'input':{'cards':[11],'query':''},'output':0}
#tests.append(test)
tests.append({'input':{'cards':[55, 56, 54, 53, 52, 51],'query':14},'output':3})
tests.append({'input':{'cards':[55, 56, 54, 53, 52, 51],'query':54},'output':2})

''' test case for checking in  a coding round, using multiple cases to check the code'''
'''using ** allows python interpreter to take the dictionary keys as inputs of the function'''
for i in range(len(tests)):
    if locate_cards(**tests[i]['input']) == tests[i]['output']:
        print(f"Test case passed and position is {locate_cards(**tests[i]['input'])}")
    else:
        print("Test case failed")
