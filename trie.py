from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.value = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.size = 0

    def put(self, key: str, value=None):
        if not key:
            raise ValueError("Key must be a non-empty string")

        current = self.root
        for char in key:
            current = current.children[char]
        if current.value is None:
            self.size += 1
        current.value = value

    def get(self, key: str):
        if not key:
            raise ValueError("Key must be a non-empty string")

        current = self.root
        for char in key:
            if char not in current.children:
                return None
            current = current.children[char]
        return current.value

    def get_all_words(self, node=None, prefix=""):
        if node is None:
            node = self.root

        words = []
        if node.value is not None:
            words.append(prefix)

        for char, child_node in node.children.items():
            words.extend(self.get_all_words(child_node, prefix + char))

        return words

    def keys_with_prefix(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]

        words = []

        def dfs(node, prefix):
            if node.value is not None:
                words.append(prefix)
            for char, child in node.children.items():
                dfs(child, prefix + char)

        dfs(current, prefix)
        return words