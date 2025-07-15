import random

Sentence =  [["나는", "학교에", "간다"], ["내가", "니", "애비다"], ["집에", "가고", "싶다"],["버스를", "빨리", "타자"],["실기를", "한방에", "합격하자"],
            ["오늘의", "메뉴는", "뭐일까"], ["밥은", "먹고", "해야지"], ["내일", "비가", "올까?"]]
count = 0

for i in range(5):
    Pick_up = random.choice(Sentence)
    Pick_up_shuffle = Pick_up[:]

    random.shuffle(Pick_up_shuffle)
    Pick_up = Pick_up[0]+" "+Pick_up[1]+" "+Pick_up[2]
    print(Pick_up_shuffle)


    Answer = input("올바른 순서로 입력하세요 : ")

    if Answer == Pick_up:
        print("정답입니다.")
        count += 1
    else:
        print("오답입니다.")


print(f"성공횟수는 {count}입니다.")

