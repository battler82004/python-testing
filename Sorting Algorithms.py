# James Taddei
# "Best" Sorting Algorithms
# 3/25/21

# Import Statement
import random

# Main Function Which Goes through Inputs, Calling the Relevant Functions, and the Final Print Statements
def main():
    # Variable Creation + Inputs
    preSort = input("Enter the list separated by spaces or just press enter to use a default list (bogosort only works well when the list is less than 10 elements):\n\n")
    if (preSort == ""):
        preSort = ["How", 1, "do", 7, "you", "9", "do", "2", "fellow"]
    else:
        preSort = preSort.split(" ")
    
    route = int(input("Enter the number for the sorting algorithm you would like to use:\n1. Bogosort\n2. Stalin sort\n3. My Sort\n\n"))
    
    # These statements tell the program which function to call
    if (route == 1):
        print(bogo_sort(preSort))
    elif (route == 2):
        print(stalin_sort(preSort))
    elif (route == 3):
        print(my_sort(preSort))
    else:
        print ("Error, that input is not valid\nRestarting the program")
        main()

# Program will often time out if len(preSort) >= 10
# This function is a BogoSort algorithm (sorts a list via creating random variations)
def bogo_sort(preSort):
    # Variable Creation
    notSorted = True
    tempList = []
    testingList = preSort

    # This while loop actually goes through the process of sorting the list
    while (notSorted):
        # This segment constantly creates different random versions of the list (w/o using shuffle cause am dumb)
        tempList = testingList
        testingList = []
        for i in range(len(tempList)):
            maximum = len(tempList)
            pos = random.randint(0,(maximum-1))
            testingList.append(tempList[pos])
            del tempList[pos:(pos+1)]
        
        # This loop checks if the current version of the list is sorted or not
        for index in range(len(testingList) - 1):
            notSorted = False
            # Test each position for being less than the next, set 'notSorted' to False if true
            if (testingList[index] > testingList[(index + 1)]):
                notSorted = True
                break
    
    # Final return statement
    return (testingList)
    
# This function sorts a list by deleting elements which are out of place
def stalin_sort(preSort):
    # This segment removes elements which are out of place in the list to "sort" the list
    notSorted = True
    while notSorted:
        for pos in range(len(preSort)):
            if (pos < (len(preSort) -1)):
                if (preSort[pos] > preSort[(pos + 1)]):
                    del preSort[pos:(pos + 1)]
                    
        # This loop checks if the current verion of the list is sorted or not
        for index in range(len(preSort) - 1):
            notSorted = False
            # Test each position for being less than the next, set 'notSorted' to False if true
            if (preSort[index] > preSort[(index + 1)]):
                notSorted = True
                break
                
    # Final return statement
    return (preSort)

# This function sorts the list by taking elements from the old one and adding it to the new one
def my_sort(preSort):
    finalList = []
    
    # This loop sorts the list
    for item in preSort:
        shouldInsert = True
        # This section adds elements to 'finalList' when the number of elements >=3
        if (len(finalList) >= 3):
            pos = 0
            # This loop finds where the item needs to be added
            while item >= finalList[pos]:
                if (pos == (len(finalList) - 1)):
                    finalList.append(item)
                    shouldInsert = False
                    break
                    
                pos += 1
                
            # This section adds the item to the list if it isn't the new greatest item
            if (shouldInsert):
                finalList.insert(pos, item)
                
        # These segments if <3 items are in 'finalList'
        elif (len(finalList) == 0):
            finalList.append(item)
        elif (len(finalList) == 2):
            if (item <= finalList[0]):
                finalList.insert(0, item)
            elif (item <= finalList[1]):
                finalList.insert(1, item)
            else:
                finalList.append(item)
        elif (item >= finalList[0]):
            finalList.append(item)
        else:
            finalList.insert(0, item)
            
    # Final return statment
    return (finalList)
    
# This call starts the actual scripts
main()