#3단어로 구성된 문장 3중리스트 생성 ,랜덤 함수 사용, 질문으로 출력 정답 체크 출력, 5회 진행 성공횟수 출력
# 장병훈 
import random

sen = [['나는','학교를','간다'],['나는','운동을','간다'],['나는','집으로','간다'],['나는','바보','입니까?'],['나는','바보가','아닙니다']]

print("올바른 한글 문장 만들기")
score = 0

for total in range(5):
    sel_sen = random.choice(sen)
    shu_sen = sel_sen[:]
    random.shuffle(shu_sen)

    print(' '.join(shu_sen))

    answer = input("올바른 문장을 입력하시오").strip()
    correct = 0
    cor_sen = ' '.join(sel_sen)
    if answer == cor_sen:
        print("정답")
        score += 1
    else:
        print("오답")
print(f'성공한 횟수:{score}')