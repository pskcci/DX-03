#11번 서준희
import random

sen = [
    ["나는","학교를","간다"],
    ["나는","햄버거를","먹는다"],
    ["너는","무엇을","하니?"],
    ["조카는","상어를","좋아한다"],
    ["나는","교정을","하고있다"],
    ["나는","시력교정을","했다"],
    ["할머니는","완전","짠순이다"],
    ["아빠는","미국에","있다"],
    ["엄마는","혼자","산다"],
    ["오빠는","공부를","좋아한다"],
    ["나는","공부를","좋아하지않는다"],
    ["나는","돈이","좋더라"]
]

score=0
for total in range(5):
    word_list = random.choice(sen)
    shuffle = random.sample(word_list,k=len(word_list))
    print("문제: ",shuffle)

    user_input = input("올바른 문장으로 만드시오\n").strip("")
    word = ' '.join(word_list)

    if user_input == word:
        score+=1
        print("정답입니다.\n")
    else:
        print("틀렸습니다!\n")

print(f"{total+1} 문제 중 {score}개 맞았습니다!")
    