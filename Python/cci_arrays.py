#Given two strings checks if they are permutations of each other:
def checkPermutation (string1, string2): 
    string1_length = len(string1)
    string2_length = len(string2)
    if (string1_length != string2_length):
        return False
    string1 = sorted(string1)
    string2 = sorted(string2)
    
    for x in range(0, string1_length, 1):
        if (string1[x] != string2[x]):
            return False
    return True

""" if (checkPermutation("test", "tset")):
    print("True")
else:
    print("False") """

#Given unsorted list, find the frequency of each character
def countFreq(unlist):
    frequency = {}
    for n in unlist:
        if n in frequency:
            frequency[n] += 1
        else:
            frequency[n] = 1
    for key, value in frequency.items():
        print ("%d : %d" %(key, value))
unlist =  [1,3,5,6,7,8, 5, 64, 6, 7,7,8, 777, 23, 1, 4, 5, 88, 88, 7]
countFreq(unlist)

#Given a string and its true lenght return a replace all spaces in string with "%20"
#This is really easy in Python, should try to implement in Java or something else 
def urlify (string, string_length): 
    urled = string.replace(" ", "%20")
    print (urled)
urlify("This is a Te3t   ", 1) 

