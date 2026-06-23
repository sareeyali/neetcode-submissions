class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = []
        self.keys[key].append([timestamp, value])


    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.keys:
            curr = self.keys[key] # curr is = to a list of pairs
            l = 0
            r = len(curr) - 1
            while l <= r:
                m = (l + r) // 2
                if curr[m][0] <= timestamp:
                    res = curr[m][1]
                    l = m + 1
                else:
                    r = m - 1
        return res
