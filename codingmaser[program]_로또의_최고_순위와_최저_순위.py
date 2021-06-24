def solution(lottos, win_nums):
    answer = []
    # 당첨번호와 몇 개가 같은지 세어줍니다.
    count = 0
    # 알수없는 번호가 몇 개인지 세우줍니다.
    num_0 = 0

    # 내 번호를 하나씩 뽑아옵니다.
    for n in lottos:
        if not n:
            num_0 += 1

        elif n in win_nums:
            count += 1
    # 당첨번호와 둘 이상의 수가 같다면
    # 예상 등수는 7 - max, 7 - min 이 됩니다.
    if count > 1:
        answer.append(7-(count+num_0))
        answer.append(7-count)

    # 당첨번호와 같은 수가 하나 이하여도
    # 알 수 없는 수를 합쳤을때 2개 이상이라면 아래와 같이
    # 최고, 최저 등수를 예상할 수 있습니다.
    elif count+num_0 > 1:
        answer.append(7-(count+num_0))
        answer.append(6)
    else:
        answer.append(6)
        answer.append(6)

    return answer

'''다른사람풀이
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
'''
