class TrieNode:
    __slots__ = ('children', 'is_end_of_word', 'sum')  # saves memory
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False
        self.sum = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.exist = {}

    @staticmethod
    def _idx(ch: str) -> int:
        return ord(ch) - 97  # 'a' -> 0

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for ch in key:
            i = self._idx(ch)
            child = node.children[i]
            if child is None:
                child = TrieNode()
                node.children[i] = child
            node = child
            if key in self.exist:
                diff = self.exist[key] - val
                node.sum = node.sum - diff
            else:
                node.sum += val
        self.exist[key] = val
        node.is_end_of_word = True

    def sum(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            node = node.children[self._idx(ch)]
            if node is None:
                return 0
        return node.sum


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)