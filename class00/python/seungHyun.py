#작성자:  이승현
import random
li1 =[["나는","학교를","간다"],["오늘은","집에","간다"],["약속을","반드시","지키자"],["내일","학교에","간다"],["아침은","반드시","온다"],["새벽에","산을","올랐다"],["내일은","상공회의소를","간다"],["방학은","한달뒤","끝난다"]]

score = 0
for i in range(5):
    li2 = []
    word1 ,word2, word3 = random.choice(li1) 

    li2.append(word1)
    li2.append(word2)
    li2.append(word3)
    li1.remove(li2)
    answer = " ".join(li2)
    random.shuffle(li2)
    print("문제 {0}번".format(i+1))
    print("다음 단어들을 올바른 순서로 조립하세요")
    for y in li2:
        print(y,end=" ")
    user_input = (input("\n정확한 문장을 입력해주세요.: "))

    if answer == user_input:
        print("정답입니다.")
        score += 1
    else:
        print("틀렸습니다.")
print("게임종료 총점 : {0}점".format(score))




