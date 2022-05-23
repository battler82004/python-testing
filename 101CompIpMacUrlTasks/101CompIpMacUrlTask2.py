# James Taddei
# 101Computing IP, MAC, and URL Python Task #2
# 5/23/22

"""
    Description:
    Write a python program that asks the user to enter a URL. The program will then extract
    and output the following components of the URL:
        Protocol
        Domain name
        Folder structure
        File name

    https://www.101computing.net/ip-addresses-ipv4-ipv6-mac-addresses-urls/
"""

def main():
    # User input
    url = raw_input("Enter a URL to be examined: ")
    url = url.split("/")

    print("Protocol: " + url[0][0:len(url[0])-1])
    print("Domain name: " + url[2])

    # Folder struct
    folderStruct = ""

    if (len(url) > 4): # Checks if there is a folder structure
        if (len(url) == 5): # Only one folder
            folderStruct = url[3]
        else: # Multiple folders
            for i in range(3,len(url)-1):
                folderStruct += url[i] + "/"
                
            folderStruct = folderStruct[0:len(folderStruct)-1] # Removes for slash at the end
    else: # No folder structure
        folderStruct = "N/A"

    print("Folder structure: " + folderStruct)

    # File name
    if (url[-1] == ""): # If there's no specified file
        fileName = "index.html"
    else:
        fileName = url[-1]

    print("File name: " + fileName)

main()
