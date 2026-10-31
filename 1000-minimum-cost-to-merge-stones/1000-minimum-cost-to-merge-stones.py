class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)

        if (n - 1) % (k - 1) != 0:
            return -1

        pre = [0] * (n + 1)
        for i, v in enumerate(stones):
            pre[i + 1] = pre[i] + v

        memo = {}

        def f(i, j):
            if i == j:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            best = float('inf')
            m = i

            while m < j:
                best = min(best, f(i, m) + f(m + 1, j))
                m += k - 1

            if (j - i) % (k - 1) == 0:
                best += pre[j + 1] - pre[i]

            memo[(i, j)] = best
            return best

        return f(0, n - 1)