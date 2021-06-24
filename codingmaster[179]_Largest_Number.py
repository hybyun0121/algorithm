from collections import Counter

class Solution:
    def compare_nums(self, n1, n2):
        if n1+n2 > n2+n1:
            print(n1, n2)
            return n1, n2
        elif n1+n2 == n2+n1:
            return min(n1,n2), max(n1,n2)
        else:
            print(n2, n1)
            return n2, n1



    def largestNumber(self, nums):
        if sum(nums) == 0:
            return "0"

        str_list = sorted(list(map(lambda x : str(x),nums)), reverse=True)
        cun_dict = Counter(str_list)
        sol_list = []

        for (s, n) in cun_dict.items():
            tmp = ''
            for _ in range(n):
                tmp += s
            sol_list.append(tmp)

        sol = ''

        i=0
        while i < len(sol_list)-1:
            j = i
            while j < 0:
                sol_list[i], sol_list[i+1] = self.compare_nums(sol_list[j-1],sol_list[j])
                j -= 1
            i += 1

        for s in sol_list:
            sol += s
        return sol

sol = Solution()

nums = [93,51,65,84,91,78,99,71,97,9]
sol.largestNumber(nums)
