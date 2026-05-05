class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [[temperatures[-1],len(temperatures)-1]]
        result = [0 for i in range(len(temperatures))]
        for i in range(len(temperatures)-2,-1,-1):
            print(stack)
            temp = temperatures[i]
            while stack and stack[-1][0] <= temp:
                stack.pop()
            if not stack:
                result[i] = 0
            else:
                result[i] = stack[-1][1]-i
            stack.append([temp,i])
        return result

    
    #[30,38,30,36,35,40,28]

    #[1,4,1,2,1,0,0]
            