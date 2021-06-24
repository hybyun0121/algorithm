class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter

        ana_dict = {}
        for str in strs:
            # 빈 리스트를 value 값으로 정해주는 메소드
            ana_dict.setdefault(str, [])
            # 단어를 key로 하고 단어를 정렬하여 value로 넣어준다.
            ana_dict[str].append(''.join(sorted(str)))
        # 위와 같이 value를 리스트로 하는 이유는 똑같은 단어여도 중복을 허용하기 위함이다.
        # 예를 들면 eat, eat 이면 aet가 두 번 존재하는 것이다.

        # value를 기준으로 정렬한다.
        sorted_ana = sorted(ana_dict.items(), key=lambda x: x[1][0], reverse=True)

        # 같은 value 값을 가지는 key들을 하나의 list에 담아준다.
        _temp = {}
        for key, value in sorted_ana:
            _temp.setdefault(value[0], [])
            for _ in range(len(value)):
                _temp[value[0]].append(key)
        _temp
        _list = [v for _, v in _temp.items()]
        return _list

# sorted_ana
# same_word = []
# _list = []
# word, ana = sorted_ana.pop()
# same_word.append(word)
#
# while sorted_ana != []:
#     word_next, ana_next = sorted_ana.pop()
#     if ana == ana_next:
#         same_word.append(word_next)
#     else:
#         _list.append(same_word)
#         same_word = []
#         word, ana = word_next, ana_next
#         same_word.append(word)
# _list
# _list.append(same_word)
