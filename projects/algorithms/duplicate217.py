# Given an integer array return true if any value appears twice else false.
#[1,2,1,3] return True, [1,2,3] return False
# sorting the array would make it easy to identify - nlogn
# Keep track of all elements seen and quickly.
#Hashset


from logging_config import get_logger

logger = get_logger(__name__)

def duplicate(x):
    all = set(x)
    if len(all) != len(x):
        return True
    else:
        return False
print(duplicate([1,2,1,3]))