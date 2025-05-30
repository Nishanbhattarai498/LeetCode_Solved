class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def get_distances(start):
            n = len(edges)
            dist = [-1] * n
            current = start
            distance = 0
            while current != -1 and dist[current] == -1:
                dist[current] = distance
                distance += 1
                current = edges[current]
            return dist

        dist1 = get_distances(node1)
        dist2 = get_distances(node2)
        
        result_node = -1
        min_max_dist = float('inf')
        
        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:
                max_dist = max(dist1[i], dist2[i])
                if max_dist < min_max_dist:
                    min_max_dist = max_dist
                    result_node = i
                elif max_dist == min_max_dist and i < result_node:
                    result_node = i
        
        return result_node
