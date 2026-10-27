class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            if i not in seen:
                seen[i] = 0
            seen[i] += 1
        pairs = list(seen.items())
        sorted_pairs = sorted(pairs, key=lambda x: x[1],            reverse=True)
        cut = sorted_pairs[:k]
        print(cut)

        val = []
        for j in cut:
            val.append(j[0])

        return val
            


        

