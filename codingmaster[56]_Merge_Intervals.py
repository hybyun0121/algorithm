class Solution:
    def merge(self, intervals):
        sorted_list = sorted(intervals, key=lambda x : x[0])
        sol, tmp = [], []
        max_idx = len(sorted_list) - 1
        tmp.append(sorted_list[0][0])
        i,j = 0, 1

        print(tmp[-1])
        print(sorted_list[-1][1])
        while tmp[-1] < sorted_list[-1][1]:
            if sorted_list[i][1] >= sorted_list[j][0]:
                if sorted_list[i][1] < sorted_list[j+1][0]:
                    tmp.append(sorted_list[i][1])
                    tmp.append(sorted_list[j][0])
                    tmp.append(sorted_list[j][1])
                    tmp.sort()
                    sol.append([tmp[0],tmp[-1]])
                    tmp=[]
                    i = j
                    j += 1
                    j = min(j, max_idx)
                else:
                    j+=1
            else:
                tmp.append(sorted_list[i][1])
                tmp.sort()
                sol.append([tmp[0],tmp[-1]])
                tmp=[]

                i += 2
                i = min(i, max_idx)
        print(sol)



s = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
s.merge(intervals)
