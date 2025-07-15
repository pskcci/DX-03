#하진영
import random
words=[
    ["나는","잠을","잔다"],
    ["짱구는","밥을","먹는다"],
    ["맹구는","수영을","한다"]
]

game_count = 5
score = 0

for i in range(game_count):
    print()
    sel_words = random.choice(words)
    out_words = sel_words[0]+" "+sel_words[1]+" "+sel_words[2]
    random_words = random.sample(sel_words,3)
    print("제시문장:",end=' ')
    for j in random_words:
        print(j,end=" ")
    user_words = input("\n 입력:")
    if user_words == out_words:
        print("올바른 문장.\n")
        score += 1
    else:
        print(f"바른문장 : {out_words}.\n")

print(f"성공횟수 {score}")

   