
def locate_cards(cards,query):
    if len(cards) == 0:
        print('Deck is empty')
    elif cards[0] == query:
            print(0)
    elif cards[-1] == query:
            print(len(cards)-1)
    else:
        for i in range(len(cards)):
            if cards[i] == query:
                print (i)
    

cards = [3,11,10,21]
''' test case for checking in  a coding round'''
#query = 7
#output = 3
locate_cards(cards,10)
