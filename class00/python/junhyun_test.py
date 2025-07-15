#3단어로 구성된 문장을 3중 리스트 생성 
#랜덤하게 한 문장을 선택 (중복선택허용)
#선택된 문장을 섞어서 실문으로 출력
#게임 유저가 올바른 문장으로 입력후 맞았는지 틀리는지 확인 
#총 5회 게임이 진행 되고 성공한 횟수 출력후 종료


#04번 김준현

import random

# 3단어로 구성된 문장 리스트
sentences = [
    ["나는", "밥을", "먹었다"],
    ["고양이가", "의자에", "앉았다"],
    ["하늘이", "매우", "맑다"],
    ["친구와", "영화를", "봤다"],
    ["책을", "조용히", "읽는다"],
    ["강아지가", "공을", "물었다"],
    ["엄마가", "저녁을", "차렸다"],
    ["바람이", "시원하게", "분다"],
    ["아이가", "웃으며", "달린다"],
    ["선생님이", "학생을", "칭찬했다"]
]

score = 0
rounds = 5

print(" 문장을 올바르게 정렬하세요! (총 5문제)\n")

for i in range(rounds):
    quiz = random.choice(sentences)
    shuffled = quiz[:]
    random.shuffle(shuffled)
    while shuffled == quiz:
        random.shuffle(shuffled)

    print(f"{i+1}번 문제입니다 : {' / '.join(shuffled)}")
    user_input = input("정확한 순서로 고치세요: ").strip().split()

    if user_input == quiz:
        print(" 정답입니다!\n")
        score += 1
    else:
        print(f" 틀렸습니다. 정답: {' / '.join(quiz)}\n")

print(f" 게임 종료! 당신의 점수: {score}/{rounds}")