def solution(new_id):
    import re
    answer = ''
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9-_.]','',new_id)

    l,r=0,1
    while r <= len(new_id):
        if new_id[l] == '.':
            while new_id[r] == '.':
                r += 1
                if r >= len(new_id):
                    break
            new_id = new_id.replace(new_id[l:r],'.')
        l = r
        r += 1
    new_id = dot_check(new_id)

    if not new_id:
        return "aaa"
    if len(new_id) < 3:
        for _ in range(3-len(new_id)):
            new_id += new_id[-1]
    elif len(new_id) > 15:
        new_id = new_id[:15]
        new_id = dot_check(new_id)

    return new_id

def dot_check(sen):
    if sen[0] == '.':
        sen = sen[1:]
    elif sen[-1] == '.':
        sen = sen[:-1]
    return sen

solution("=.=")
