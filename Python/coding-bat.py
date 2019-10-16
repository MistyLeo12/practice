#Delete charachter in a strings specific index
def remove_char (given, n):
    front = given[:n]
    back = given[n+1:]
    print (front + back)
print ("Test for Deleting Character at specific index:")
test = "Testing Purpose"
ind = 3
print ("Original String: " + test + " Index: "+ str(ind))
remove_char(test, ind)

#Swapping First and Last Character
def front_back(str):
    if len(str)<=1:
        return str
    mid = str[1:-1]
    print (str[-1]+mid+str[0])
print ("Test for Swapping Frist and Last Character:")
test = "Hello World"
print ("Original String: " + test)
front_back(test)

#Expand a string for each index it has ex. Given: "String" Output: "SStStrStriStrinString"
def string_expansion(str):
    output = ""
    for i in range(len(str)):
        output = output + str[:i+1]
    print (output)
string_expansion("Gabriel")

#Return every other character in a given string
def every_other(str):
    output = ""
    for i in range(len(str)):
        if i % 2 == 0:
            output = output + str[i]
    print (output)
every_other("Testing Testing, This is just a Test")

