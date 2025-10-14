class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            norm = ord(char) - ord("a")
            if cur.children[norm] is None:
                cur.children[norm] = TrieNode()
            cur = cur.children[norm]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            norm = ord(char) - ord("a")
            if cur.children[norm] is None:
                return False
            cur = cur.children[norm]
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            norm = ord(char) - ord("a")
            if cur.children[norm] is None:
                return False
            cur = cur.children[norm]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)