# James Taddei
# Target Sum Indeces
# 10/31/22

"""
Finds and outputs the indeces of the values in the list which
add up to the target value. If none are found, outputs that.
"""

def main():
    nums = [2, 7, 11, 15]
    pos1, pos2 = targetIndeces(nums, 9)
    if (pos1 is not None):
        print(f"The indeces are: {pos1} and {pos2}.")
    else:
        print(f"There aren't numbers that add up to the target.")
    
def targetIndeces(nums, target):
    """
    Returns the indeces of the numbers in nums which add up to the
    target value. If there are none, returns a tuple with 2 'None's.
    """
    numsDict = {}
    for pos, num in enumerate(nums):
        numsDict[num] = pos
    
    for pos, num in enumerate(nums):
        needed = target - num
        if ((needed in numsDict) and (numsDict[needed] != pos)):
            return (pos, numsDict[needed])
    return (None, None)
            
main()