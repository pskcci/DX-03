#kangbusic

import random

# 3단어로 구성된 문장 리스트
sentences = [
    ["나는", "학교를", "간다"], ["아빠가", "죽을", "만든다"], ["철수와", "티비를", "본다"], ["나는", "학원을", "간다"],
    ["엄마가", "밥을", "만든다"], ["친구와", "영화를", "본다"],["저는", "태권도를", "간다"], ["삼촌은", "죽을", "만든다"], ["수진과", "넷플릭스를", "본다"], 
    ["저희는", "교회을", "간다"],  ["이모가", "쌈을", "만든다"], ["애인과", "영화를", "본다"]
]

# 성공 횟수 기록
scount = 0

# 5회 게임 반복
for i in range(5):
    # 문장 랜덤 선택 (중복 허용)
    selected = random.choice(sentences)
    words = selected.copy()

    # 단어 섞기
    random.shuffle(words)
    print(f"\n다음 단어들을 올바른 순서로 조합하세요: {' '.join(words)}")

    # 사용자 입력
    user_input = input(">> ")

    # 맞는지 확인
    if user_input.strip() == ' '.join(selected):
        print("정답입니다!")
        scount += 1
    else:
        print(f"틀렸습니다. 정답: {' '.join(selected)}")

# 최종 결과 출력
print(f"\n총 {scount}회 성공하였습니다.")