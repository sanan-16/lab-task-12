class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

# Example usage
trie = Trie()
words_to_insert = ["apple", "app", "banana", "orange", "grape"]

for word in words_to_insert:
    trie.insert(word)

search_word = "apple"
print(f"Is '{search_word}' in the trie? {trie.search(search_word)}")

search_word = "apples"
print(f"Is '{search_word}' in the trie? {trie.search(search_word)}")
