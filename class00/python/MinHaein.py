#3반- 민해인
#올바른 한글 문장 만들기!
#요구사항

import random

msg_lst = [['나는','학교에','간다'], ['우리는','여행을','떠난다'], ['언니는','밥을','좋아한다'],
           ['고양이가','털공을', '굴린다'], ['내일부터', '방학이라', '놀러간다'],
           ['오리가', '물위에', '떠간다'], ['바가지에','물이','샌다'], ['수학은','언제나','즐겁다']]

count =0
correct = 0
user_input = []

for i in range(5): #5회 반복
    text = ""
    print("*"*50)
    print(f"{i+1}번 문제")
    print("*  다음 단어들을 올바른 순서로 조합하세요  *")

    text = random.choice(msg_lst) #랜덤으로 문장을 선택
    msg_lst.remove(text) #중복방지
    correct_text = ' '.join(text)

    random.shuffle(text)
    print("*"*50)
    print(' '.join(text))
    

    user_input = input("정확한 문장을 입력하시오:")

    print("")

    if user_input == correct_text:
        print("정답입니다.")
        correct += 1
    else:
        print("오답입니다.")
    


print(f"게임 종료! 총 {correct}문제를 맞췄습니다.")
