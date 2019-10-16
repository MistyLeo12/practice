# Node class 
class Node: 
    # Initialize the node object 
    def __init__(self, val): 
        self.val = val  # Assign val 
        self.next = None  # Initialize next as null 
   
# Linked List class 
class LinkedList: 
    # Initialize the Linked List
    def __init__(self):  
        self.head = None
    def printList(self): 
        temp = self.head 
        while (temp): 
            print (temp.data) 
            temp = temp.next