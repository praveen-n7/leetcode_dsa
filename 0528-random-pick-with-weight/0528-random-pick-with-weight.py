import random

class Solution:

    def __init__(self, w):
        self.w = w
        self.total = sum(w)

    def pickIndex(self):
        r = random.randrange(self.total)
        acc = 0

        for i, x in enumerate(self.w):
            acc += x
            if acc > r:
                return i

        return len(self.w) - 1