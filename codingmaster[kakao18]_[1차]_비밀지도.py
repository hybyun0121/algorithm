bin(10)
bin(9)
bin(30)
9|30
bin(31)

def solution(n, arr1, arr2):
    answer = []

    setting = ""
    for i,j in zip(arr1, arr2):
        overlap = i|j # 하나라도 1이면 1이므로
        full_map = bin(overlap)[2:] #'0b....'에서 0b 필요 X

        full_map = full_map.replace("1","#")
        full_map = full_map.replace("0"," ")

        # 아래 두 줄을 str.rjust(n,' ')로 대체가능하다.
        length = n - len(full_map)
        full_map = " "*length + full_map
        answer.append(full_map)

    return answer

a = "1010"
a.rjust(5,' ')

overlap = 31|14
overlap
bin(31)
bin(14)

"#" * 5
"ㅁ" +" "
