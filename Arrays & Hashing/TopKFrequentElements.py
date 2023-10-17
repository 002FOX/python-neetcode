# Hashmap for storing the element with its frequency, then we use bucketsort with the indices of the array being the frequencies, 
# so the max frequency should be the size of the array, obviously you can sort normally instead and just get the top K keys in the hashmap
# Time : O(n) 2n + k 
# Space : O(n) hashmap: n, frequency: n, elements: k
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        for x in nums:
            count[x]= 1 + count.get(x, 0)
        
        frequency = [[] for i in range(len(nums) + 1)] 

        for key, v in count.items():
            frequency[v].append(key)
        
        elements = []
        for i in range(len(frequency) - 1, 0, -1):
            for j in frequency[i]:
                elements.append(j)
                if len(elements) == k:
                    return elements