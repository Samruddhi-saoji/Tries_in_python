from trie import Trie #import module

#driver code 
trie = Trie()

# Insert words into the trie
trie.insert("apple")
trie.insert("carpet")
trie.insert("aeroplane")
trie.insert("dog")

# Search 
print(trie.search("apple"))   # T
print(trie.search("dogs"))    # F

print(trie.search("car")) # word "car" is not present 
print(trie.search_prefix("car")) # prefix "car" is present

# Check if any word in the trie starts with the given prefix
print(trie.search_prefix("app"))  # T
print(trie.search_prefix("b"))    # F
print(trie.search_prefix("d"))    # T
