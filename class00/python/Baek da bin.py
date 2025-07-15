# 작성자 백다빈

import random

sel = [["하룻", "강아지" ,"짖는다"],
      ["도둑이", "제발", "저리다"],
      ["등잔", "밑이", "어둡다"],
      ["원숭이도", "나무에서", "떨어진다"],
      ["낮말은", "새가듣고", "밤말은쥐가듣는다"],
      ["고래", "싸움에", "새우등터진다"],
      ["작은", "고추가", '더맵다'],
      ["가는말이", "고와야오는", "말이곱다"],
      ["공든", "탑이", "무너지랴"],
      ["누워서","떡","먹기"]]


score = 0

for b in range(5):
    part = random.choice(sel)
    ok = "".join(part)
    
    shuf = part[:]
    random.shuffle(shuf)
    print(f"문제 {b+1}:{"/".join(shuf)}")
    print("다음 단어들을 올바르게 정렬해 주세요")
    user = input("문장을 입력해 주세여 : ").strip()

    if user == ok:
        print("정답입니다!\n")
        score += 1
    else:
        print(f"틀렸습니다. 정담은:{ok}\n")
print(f"게임종료 ! 최종 스코어는 : {score}문제 성공!")