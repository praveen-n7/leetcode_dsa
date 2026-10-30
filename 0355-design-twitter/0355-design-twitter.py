import heapq

class Twitter:

    def __init__(self):
        self.t = 0
        self.tweets = {}
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.setdefault(userId, []).insert(0, (self.t, tweetId))
        self.t += 1

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows.get(followerId, set()).discard(followeeId)

    def getNewsFeed(self, userId: int) -> List[int]:
        fans = set(self.follows.get(userId, ())) | {userId}
        h = []

        for f in fans:
            tw = self.tweets.get(f, [])
            if tw:
                heapq.heappush(h, (-tw[0][0], tw[0][1], f, 0))

        out = []
        while h and len(out) < 10:
            ts, x, f, i = heapq.heappop(h)
            out.append(x)

            tw = self.tweets.get(f, [])
            if i + 1 < len(tw):
                heapq.heappush(h, (-tw[i + 1][0], tw[i + 1][1], f, i + 1))

        return out