class TrieNode:
    def __init__(self):
        self.children = {}
        self.documents = set()

class TagTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert_document(self, document_id, tags):
        for tag in tags:
            self._insert_tag(document_id, tag)

    def _insert_tag(self, document_id, tag):
        node = self.root
        for char in tag:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.documents.add(document_id)

    def search_documents_by_tag(self, tag_prefix):
        node = self.root
        for char in tag_prefix:
            if char not in node.children:
                return set()  # No documents found for the given tag prefix
            node = node.children[char]

        return node.documents

# Example Usage
tag_trie = TagTrie()

# Inserting documents with tags
tag_trie.insert_document(1, ["programming", "python", "data-structures"])
tag_trie.insert_document(2, ["programming", "java", "algorithms"])
tag_trie.insert_document(3, ["machine-learning", "python", "data-science"])

# Searching for documents with a specific tag prefix
tag_prefix = "python"
result_documents = tag_trie.search_documents_by_tag(tag_prefix)

print(f"Documents with tag prefix '{tag_prefix}': {result_documents}")
