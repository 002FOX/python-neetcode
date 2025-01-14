import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        result = []

        for x in nums:
            counter[x] = 1 + counter.get(x, 0)
        
        # Normal Sorting O(nlogn)
        sorted_tuples = sorted(counter.items(), key= lambda tuple: tuple[1], reverse=True)
        for x in range(k):
            result.append(sorted_tuples[x][0])
        result = []

        # Bucket Sort O(n)
        frequency = [[] for i in range(len(nums) + 1)]
        for key, value in counter.items():
            frequency[value].append(key)
        for i in range(len(frequency) - 1, 0, -1):
            for j in frequency[i]:
                result.append(j)
                if len(result) == k:
                    break
            if len(result) == k:
                break
        result = []

        # Heap O(nlogk) ~O(n)
        heap = []
        for x, freq in counter.items():
            heapq.heappush(heap, (freq*-1, x)) # Negative numbers to simulate a max heap using the built-in min heap
        print(heap)

        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result
