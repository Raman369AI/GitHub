
from logging_config import get_logger

logger = get_logger(__name__)

source = [5]
auxillary = []
target = []
n = len(source)


'''
Towers of hanoi:
n == 1: Move the one disc to the target rod:
n == 2: Move the top to Auxillary and the bottom to the target and then send the auxiallary disk to target.
n == 3: Treat the top 2 as one disc and the bottom as another, in the top 2 
treat as if they only exist and making sure both of them end up at  the same auxillary rod
n == 4: The top 3 as one unit and the bottom as another now treat the auxilary as the target and send the top 3 there
'''
def towers_of_brahma(n,source, auxillary, target):
    if n == 1:
        target.append(source.pop()) 
        return target
    towers_of_brahma(n-1, source, target, auxillary)
    target.append(source.pop())
    towers_of_brahma(n-1, auxillary, source, target)
    return target
print(towers_of_brahma(n,source, auxillary, target))
    