class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # log가 종류별로 정렬 방식이 다르다.
        # 종류 별로 다른 리스트에 담기 위해 빈 리스트를 만든다.
        dig_log = []
        let_log = []

        # 한 log 씩 뽑아서 식별자 다음에 오는 문자의 타입을 확인한다.
        # 숫자인 경우와 문자인 경우를 구분하여 각각 리스트에 담는다.
        for log in logs:
            if log.split()[1].isalpha() is True:
                let_log.append(log)
            else:
                dig_log.append(log)
        # 문자 로그를 sort 한다.
        let_log.sort()
        re_log = sorted(let_log, key=lambda x : x.split()[1:])

        # 숫자 로그는 입력 순서 그대로를 따르기 때문에 별다른 정렬은 필요없다.
        return re_log + dig_log
