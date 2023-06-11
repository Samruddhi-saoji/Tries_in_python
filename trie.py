class Node:
    def __init__(self):
        self.children = {} #dict of child nodes
            # {letter : Node}

        #is this letter the last letter of the word?
        self.is_last_letter = False



class Trie:
    def __init__(self):
        self.root = Node() #root of the tree


    #insert word into the trie
    def insert(self, word):
        #node for traversal
        node = self.root #current node

        #traverse each letter in the word
        for letter in word:
            #if this letter doesnt exist as a child of the current node 
            if letter not in node.children :
                #create a new child node
                node.children[letter] = Node()

            #traverse to the child node
            node = node.children[letter]

        #the current node is the last letter of the word
        node.is_last_letter = True



    #returns true if the word exists in the trie
    def search(self, word):
        #node for traversal
        node = self.root

        # Traverse each letter in the word
        for letter in word:
            #if this letter doesnt exist as a child of the current node, then 
            #this word is not in the trie
            if letter not in node.children:
                return False
            
            
            #letter is present as a child node
            #go to the child node
            node = node.children[letter]
        #all letters of the word are present in the correct sequence

        # Is the last letter node is also the end of a word?
        return node.is_last_letter
        # example: if "carpet" is present in trie, but "car" is not



    #prefix = starting letters of a word
    def search_prefix(self, prefix):
        #node for traversal
        node = self.root

        # Traverse each letter in the word
        for letter in prefix:
            #if this letter doesnt exist as a child of the current node, then 
            #this prefix is not in the trie
            if letter not in node.children:
                return False
            
            #letter is present as a child node
            #go to the child node
            node = node.children[letter]
        return True


