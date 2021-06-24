class Solution:
    from collections import Counter
     "cbacdcbc" {'c':3, 'b':1, .....}
    def removeDuplicateLetters(self, s: str) -> str:
            counter, seen, stack = collections.Counter(s), set(), []

            for char in s:
                counter[char] -= 1 # 하나 빼왔단 의미?
                if char in seen: # 이미 처리된 문자인지 확인하는 라인
                    continue

                # stack에 원소가 있고 stack의 마지막 값이 char 보다 크고
                # counter에 stack[-1]이 0보다 크다면 => 즉 뒤에서 또 나오면
                while (stack and char < stack[-1]
                        and counter[stack[-1]] > 0):
                    seen.remove(stack.pop()) # seen set에서 stack[-1]을 제거
                stack.append(char)
                seen.add(char)

            return ''.join(stack)

# http://pythontutor.com/live.html#mode=edit
# from collections import Counter
#
# def removeDuplicateLetters(s):
#         counter, seen, stack ={'c':4,'b':2,'a':1,'d':1}, set(), []
#
#         for char in s:
#             counter[char] -= 1 # 하나 빼왔단 의미?
#             if char in seen: # 이미 처리된 문자인지 확인하는 라인
#                 continue
#
#             # stack에 원소가 있고 stack의 마지막 값이 char 보다 크고
#             # counter에 stack[-1]이 0보다 크다면 => 즉 뒤에서 또 나오면
#             while (stack and char < stack[-1]
#                     and counter[stack[-1]] > 0):
#                 seen.remove(stack.pop()) # seen set에서 stack[-1]을 제거
#             stack.append(char)
#             seen.add(char)
#
#         return ''.join(stack)
#
# s = "cbacdcbc"
# removeDuplicateLetters(s)
