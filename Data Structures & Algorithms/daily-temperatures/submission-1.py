class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for i in range(len(temperatures))]
        for i in range(len(temperatures)):
            temp = temperatures[i]
            print(stack)
            while stack and stack[-1][0] < temp:
                result[stack[-1][1]] = i-stack[-1][1]
                stack.pop()
            if not stack:
                result[i] = 0
            stack.append([temp,i])
        return result

    
    #[30,38,30,36,35,40,28]

    #[1,4,1,2,1,0,0]
            