# Longest 7-Seg Word
# James Taddei
# 3/19/21

"""
Notes:
        Tom's english list is 370k words
        Can make A-F, H-J, L, N-P, R-S, T-U, Y
        Can't make G, K, M, Q, V, W, X, Z
        Tom got: dichlorodiphenyltrichloroethane <- I got too (31 letters)
        W/o I and O: supertranscendentness <- I got too + three-and-a-halfpenny (21 letters)
"""

# Main Function
def main():
    # Variable Creation
    longestWord = ""
    equalLength = []
    
    # Copies the text from 'English_Words' and finds which words contain an invalid letter 
    with open("English_Words.txt", "r") as dictionary:
        lines = (dictionary.read()).splitlines()
        # This loop goes through each word in the list and finds if it has any invalid letters. If it doesn't, the word is checked if it is long enough
        for word in lines:
            if ((word.lower()).count("g") > 0):
                continue
            elif ((word.lower()).count("k") > 0):
                continue
            elif ((word.lower()).count("m") > 0):
                continue
            elif ((word.lower()).count("q") > 0):
                continue
            elif ((word.lower()).count("v") > 0):
                continue
            elif ((word.lower()).count("w") > 0):
                continue
            elif ((word.lower()).count("x") > 0):
                continue
            elif ((word.lower()).count("z") > 0):
                continue
            # To run without I and O, remove the hashtags from the beginning of the lines below
            #elif ((word.lower()).count("i") > 0):
                #continue
            #elif ((word.lower()).count("o") > 0):
                #continue
            else:
                equalLength = lengthCheck(word, longestWord, equalLength)
                longestWord = equalLength[0]
                
        # Main return statement for the final print
        return (finalPrint(longestWord, equalLength))
                
# Function that checks if the word is long enough to be the new longest or tied for longest
def lengthCheck(word, longestWord, equalLength):
    # If the word is longer than the longest word, then 'longestWord' and 'equalLength' become just the new word
    if (len(word) > len(longestWord)):
        longestWord = word
        equalLength = [word]
    # If the word is equal in length to the longest word, then it is added to 'equalLength'
    elif (len(word) == len(longestWord)):
        equalLength.append(word)
        
    # lengthCheck return statement, sends back the list of current longest word(s)
    return (equalLength)
    
# This function creates the string that is used as a final print variable
def finalPrint(longestWord, equalLength):
    # If there are 2 longest words, this section says the words and their length
    if (len(equalLength) == 2):
        return ("The longest 7-segment words (" + str(len(longestWord)) + " letters) are: " + equalLength[0] + " and " + equalLength[1])
    # If there are more than 2 longest words, this section says the words and their length after changing the list into a singular string
    elif (len(equalLength) > 2):
        listOfWords = ""
        for index in range(len(equalLength)):
            if (index != (len(equalLength) - 1)):
                listOfWords += equalLength[index] + ", "
            else:
                listOfWords += " and " + equalLength[index]
                
        return ("The longest 7-segment words (" + str(len(longestWord)) + " letters) are: " + listOfWords)
    # If there's only 1 longest word, this statement returns it in a string with some text at the front
    else:
        return ("The longest 7-segment word (" + str(len(longestWord)) +  " letters) is: " + longestWord)

# This is the print statement that calls 'main', actually has everything run, and prints out the result
print(main())