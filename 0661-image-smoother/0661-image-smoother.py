class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        R, C = len(img), len(img[0])
        out = [[0] * C for _ in range(R)]

        for r in range(R):
            for c in range(C):
                s = cnt = 0
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        rr, cc = r + dr, c + dc
                        if 0 <= rr < R and 0 <= cc < C:
                            s += img[rr][cc]
                            cnt += 1
                out[r][c] = s // cnt

        return out