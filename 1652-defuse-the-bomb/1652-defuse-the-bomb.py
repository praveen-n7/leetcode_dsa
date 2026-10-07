class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
        if k == 0:
            return res
        step = 1 if k > 0 else -1
        K = abs(k)
        for i in range(n):
            for s in range(1, K + 1):
                res[i] += code[(i + step * s) % n]
        return res