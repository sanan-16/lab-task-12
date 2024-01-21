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

    def _find_words_with_prefix(self, node, current_prefix, result):
        if node.is_end_of_word:
            result.append(current_prefix)

        for char, child_node in node.children.items():
            self._find_words_with_prefix(child_node, current_prefix + char, result)

    def find_words_with_prefix(self, prefix):
        result = []
        node = self.root

        # Traverse the trie to the end of the prefix
        for char in prefix:
            if char not in node.children:
                return result
            node = node.children[char]

        # Perform depth-first search to find words with the given prefix
        self._find_words_with_prefix(node, prefix, result)
        return result

# Example usage
trie = Trie()
words_to_insert = ["apple", "app", "banana", "orange", "grape"]

for word in words_to_insert:
    trie.insert(word)

prefix_to_search = "app"
found_words = trie.find_words_with_prefix(prefix_to_search)

print(f"Words in the trie with prefix '{prefix_to_search}': {found_words}")
