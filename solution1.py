from collections import Counter

class Solution:
    def __init__(self, s):
        self.s = s
        self.idx = -1

    def getFirstUnique(self):
        hmap = Counter(self.s)

        for i, v in enumerate(self.s):
            if hmap[v] == 1:
                self.idx = i
                break
        
        return self.idx

if __name__ == "__main__":
    sol_obj = Solution("abca")
    idx = sol_obj.getFirstUnique()
    print(idx)
