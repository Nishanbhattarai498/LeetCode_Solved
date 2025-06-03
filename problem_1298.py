from collections import deque
from typing import List

class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int]
    ) -> int:
        n = len(status)
        owned = set(initialBoxes)
        haveKey = set()
        visited = set()
        queue = deque()

        # Enqueue initially open boxes
        for box in initialBoxes:
            if status[box] == 1:
                queue.append(box)

        totalCandies = 0

        while queue:
            box = queue.popleft()
            if box in visited:
                continue
            visited.add(box)

            # Collect candies
            totalCandies += candies[box]

            # Process keys found in the current box
            for key in keys[box]:
                if key not in haveKey:
                    haveKey.add(key)
                    if key in owned and status[key] == 0:
                        status[key] = 1
                        queue.append(key)

            # Process contained boxes
            for contained in containedBoxes[box]:
                owned.add(contained)
                if status[contained] == 1 or contained in haveKey:
                    queue.append(contained)

            # In case any previously owned box is now openable
            for b in list(owned):
                if b not in visited and status[b] == 1:
                    queue.append(b)

        return totalCandies
