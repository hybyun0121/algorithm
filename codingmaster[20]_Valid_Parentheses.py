def isValid(s):
    l = []
    _dic = {"(":")",
            "[":"]",
            "{":"}"}
    for i in range(len(s)):
        l.append(s[i])

    if l[0] in [')',']','}'] or len(l) < 2 or len(l)%2 == 1:
        return False
    

    while len(l)-2:
        print(f"list : {l}")
        target = l.pop(0)
        next = l[0]
        last = l[len(l)-1]

        # print(f"target : {target}")
        # print(f"_dic[target] : {_dic[target]}")
        # print(f"next : {next}")
        # print(f"last : {last}")

        if _dic[target] == next:
            # print("바로옆")
            l.pop(0)
        elif _dic[target] == last:
            # print("마지막")
            l.pop()
        else:
            # print("어디에도x")
            return False
    try:
        if (len(l) == 2) and (_dic[l[0]] != l[-1]):
            return False
    except:
        return False

    return True


print(isValid("(){}}{"))
