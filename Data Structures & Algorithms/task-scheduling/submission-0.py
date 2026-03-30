class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        max_heap = [-n for n in freq if n > 0]
        heapq.heapify(max_heap)

        time = 0
        q = deque() # This will hold pairs of [-count, idleTime]
        while max_heap or q:
            time += 1

            if not max_heap:
                time = q[0][1]
            else:
                count = 1 + heapq.heappop(max_heap)
                if count < 0:
                    q.append([count, time + n])
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time