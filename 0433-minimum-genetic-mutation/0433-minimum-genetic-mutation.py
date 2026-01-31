class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque([(startGene, 0)])
        visit = set([startGene])
        
        while queue:
            gene, count = queue.popleft()
            if gene == endGene:
                return count
            for neighbor in bank:
                # check if neighbor differs by exactly one character
                diff = 0
                for i in range(len(gene)):
                    if gene[i] != neighbor[i]:
                        diff += 1

                if diff == 1 and neighbor not in visit:
                    visit.add(neighbor)
                    queue.append((neighbor, count + 1))


        return -1