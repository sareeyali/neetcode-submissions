class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.pairs = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.pairs:
            self.pairs.move_to_end(key, last=True)
            return self.pairs[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.pairs and len(self.pairs) == self.capacity:
            self.pairs.popitem(last=False)
        self.pairs[key] = value
        self.pairs.move_to_end(key, last=True)
