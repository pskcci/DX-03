#작성자 : 정민수

import random

w = [["나는", "학교를", "간다"], ["나는", "파이썬", "좋아해"], ["새가", "높이", "난다"],
     ["그녀는", "케이크를", "먹는다" ], ["그들은", "축구를", "한다"], ["우리는", "휴식이", "필요해"],
     ["시간이", "빨리", "간다"], ["아이들이", "책을", "읽는다"], ["강아지가", "크게", "짖는다"]]

def words(q):
    result = ""
    for word in q:
        result += word + " "  
    result = result.strip()
    return result


count = 0
for i in range(1, 6):
    x = random.choice(w)
    k = words(x)
    random.shuffle(x)
    u = words(x)
    print("문제: ", i)
    print("다음 단어들을 올바른 순서로 조합하세요: ")
    print(u)
    t = input("정확한 문장을 입력하세요:")
    if t == k:
        count +=1
        print("정답입니다")
    else:
        print("틀렸습니다.")

print("총 ", count, "문제를 맞췄습니다.")