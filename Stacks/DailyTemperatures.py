# We keep adding elements to the stack if theyre not higher, once we find a higher value we iteratively pop the stack until the condition is not met OR the stack is empty, and for each popped element we get the current index - the popped elements index
# to get the distance between them for the output array
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        stack.append([0, temperatures[0]])
        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                answer[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            else:
                stack.append([i, temperatures[i]])
        return answer
