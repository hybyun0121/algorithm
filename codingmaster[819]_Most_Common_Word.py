class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 단어에 구두점이 붙어있으면 갯수를 세는데 방해가 된다.
        paragraph = re.sub('[^a-zA-Z]', ' ', paragraph)
        # 모든 단어를 소문자로 바꾼다.
        paragraph = paragraph.lower()
        # 이건 필요없더라
        #banned = list(map(lambda x : x.lower(), banned))

        # list에서 원소를 key로, 원소 개수를 value로 하는 dictionary를 만든다.
        dic_words = Counter(paragraph.split())

        # value를 기준으로 내림차순으로 바꾼다.
        sorted_words = sorted(dic_words.items(), key=lambda x : x[1], reverse=True)

        # 차례로 돌면서 banned word는 넘기고 아닌 단어를 바로 retrun한다.
        # 정렬을 했으니까 가장 먼저 출력되는 단어가 가장 갯수가 많을 것이다.
        for word, cnt in sorted_words:
            if not word in banned:
                return word
