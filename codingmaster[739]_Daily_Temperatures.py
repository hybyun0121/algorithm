class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        temp = []
        ndays = 0
        if len(T) == 1:
            return 0

        while len(T):
            ndays = 0
            temp.append(ndays)

            for i in range(1, len(T)):
                if T[0] >= T[i]:
                    ndays += 1
                else:
                    ndays +=1
                    temp[-1] = ndays
                    break
            T = T[1:]
        return temp

# 1000개 list에서 시간초과...
