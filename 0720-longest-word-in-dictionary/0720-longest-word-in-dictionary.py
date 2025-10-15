class TrieNode:
    __slots__ = ('children', 'is_end_of_word')  # saves memory
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def _idx(ch: str) -> int:
        return ord(ch) - 97  # 'a' -> 0
    @staticmethod
    def _char(idx: int) -> str:
        return chr(idx+ord("a"))

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            i = self._idx(ch)
            child = node.children[i]
            if child is None:
                child = TrieNode()
                node.children[i] = child
            node = child
        node.is_end_of_word = True

    def longestWord(self):
        def dfs(node, char):
            if node is not self.root:
                if (not node or not node.is_end_of_word):
                    return ""
            
            temp = ""
            for idx, child in enumerate(node.children):
                result = dfs(child, self._char(idx))
                if len(temp) < len(result):
                    temp = result
            
            return char + temp
        
        return dfs(self.root, "")


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        return trie.longestWord()