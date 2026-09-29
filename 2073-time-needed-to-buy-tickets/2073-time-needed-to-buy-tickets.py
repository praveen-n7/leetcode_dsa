from collections import deque

class Solution:

    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        q = deque(enumerate(tickets))
        served = []

        while q:
            person = q.popleft()

            
            index = person[0] # Givethis person one ticket
            tickets_left = person[1] - 1

            served.append((index, tickets_left))

           
            if tickets_left > 0: # Put them back ifthey still need   tickets
                q.append((index, tickets_left))

           
            if index == k and tickets_left == 0:
                break  # Stop when person k gets t heir last ticket

        return len(served)