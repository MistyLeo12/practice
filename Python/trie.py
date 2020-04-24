from typing import Tuple

class TrieNode(object):
    def __init__(self, char:str):
        self.char = char
        self.children = []
        self.word_finished = False #checks if last char of word
        self.counter = 1

def add(root, word: str):
    node = root
    for char in word:
        found = False
        # Search for char in the children of current node
        for child in node.children:
            if child.char == char:
                # Found so increase counter by 1
                child.counter +=1
                node = child
                found = True
                break 
        # Character not found so add new child
        if not found:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node #point node to new hcild
    node.word_finished = True

def find_prefix(root, prefix: str) -> Tuple[bool, int]:
    ## Checks and returns if the prefix exists and how many have them
    node = root
    # if root has no children, then False
    # means search in an empty trie 
    if not root.children:
        return False, 0
    for char in prefix:
        char_not_found = True
        for child in node.children:
            if child.char == char:
                #Found char in a child
                char_not_found = False
                # Assign the node as the child and break 
                node = child
        if char_not_found:
            return False, 0
    return True, node.counter 

if __name__ == "__main__":
    root = TrieNode('*')
    add(root, "gabriel")
    add(root, "gab")


    print(find_prefix(root, 'gabe'))
    print(find_prefix(root, 'gabriel'))
    print(find_prefix(root, 'ga'))
    print(find_prefix(root, 'gabriell'))

