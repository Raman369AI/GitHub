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
def locate_cards(cards,query):
    length = len(cards)-1
    position = 0
    middle = (length + position) // 2
    if  length == 0 or query == '':
            return -1
    while position <= length:
        if query == cards[middle]:
            if cards[middle] == cards[middle - 1]:
                middle = middle - 1
            else:
                return middle
        elif query > cards[middle]:
            length = middle -1
        elif query < cards[middle]:
            position = middle + 1
            middle = middle + 1
            
    return -1         


           
        
'''
1. Check the cards length or if the query is empty then return a value of -1.
2. Check the edge cases if the query is present on the first or last of the list and return the position
3. Check the middle of the cards deck, if the query is less than go right else left 
and repeat the same until the position is found expecting a descending sorted list
'''
tests = []
test = {'input':{'cards':[11],'query':''},'output':0}
tests.append(test)
tests.append({'input':{'cards':[55, 55, 54, 54, 52, 51],'query':54},'output':2})
tests.append({'input':{'cards':[54, 54, 54, 54,53, 52, 51],'query':54},'output':0})
tests.append({'input':{'cards':[54, 54, 54, 54,52, 52, 51],'query':51},'output':6})


''' test case for checking in  a coding round, using multiple cases to check the code'''
'''using ** allows python interpreter to take the dictionary keys as inputs of the function'''
with open('check.txt','a') as file:
    original_stdout = sys.stdout
    sys.stdout = file
    print('Binary Search')
    for i in range(len(tests)):
        print(f"cards: {tests[i]['input']['cards']}")
        print(f"query: {tests[i]['input']['query']}")
        if locate_cards(**tests[i]['input']) == tests[i]['output']:
            print(f"Test case passed and position is {locate_cards(**tests[i]['input'])}")
        else:
            print("Test case for no cards or query - passed")

