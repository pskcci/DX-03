# 작성자 : 조경원

import random as r

def checkAnswer(char1, char2):
    for i in range(min(len(char1), len(char2))):

        # 문자씩으로 비교 중 다르면 오답처리
        if char1[i] != char2[i]:
            print("오답!")
            return False
                
        # for문의 마지막까지 오답이 검출되지 않으면 정답 출력 및 스코어 +1
        elif i == min(len(char1), len(char2)) - 1:
            print("정답!")
            return True   

koreanList = [ 
    ["아버지가", "방에", "들어가신다"],
    ["나는", "학교를", "간다"],
    ["철수는", "영희를", "만나러 간다"],
    ["부산엔", "바다가", "있다"],
    ["어머니는", "짜장면을", "싫다고 하셨어"],
    ["대한민국은", "자유민주주의", "공화국이다"],
    ["복무신조", "우리의", "결의"],
    ["오늘의", "요일은", "수요일이다"],
    ["도서관의", "휴일은", "월요일이다"],
    ["마지막","문장은", "여기다"]
]

print("올바른 문장을 만드는 게임입니다.")
input("아무 키나 누르면 시작!")

score = 0

for i in range(5): 
    chooseList = r.choice(koreanList)
    koreanList.remove(chooseList)
    rightAnswer = chooseList[0] + " " + chooseList[1] + " " + chooseList[2]
    r.shuffle(chooseList)
    print(f"quiz : {chooseList[0]}, {chooseList[1]}, {chooseList[2]}") 
    inputAnswer = input("정답을 입력하세요.")

    if checkAnswer(rightAnswer, inputAnswer):
        score += 1

print(f"게임 결과 발표!!\n맞힌 개수 : {score}")

