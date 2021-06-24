def solution(orders, course):
    from itertools import combinations

    answer = []
    while course:
        _list = []
        _dict = {}
        c = course.pop(0)
        for a in orders:
            a = sorted(a)
            _list.extend(list(map(lambda x : ''.join(x), list(map(lambda x : list(x), list(combinations(a,c)))))))
        for ord in _list:
            if not ord in _dict:
                _dict[ord] = 1
            else:
                _dict[ord] += 1
        
    return answer

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])

list(combinations(sorted("XWZ"),2))
