def solution(participant, completion):
    import collections
    answer = ''
    par_dict = collections.defaultdict(int)
    com_dict = collections.defaultdict(int)

    for par in participant:
        par_dict[par] += 1
    for com in completion:
        com_dict[com] += 1

    for k,v in par_dict.items():
        if (v - com_dict[k]) == 1:
            return k
-----------------------------------------------
# 이걸 이렇게??
'''
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
'''
