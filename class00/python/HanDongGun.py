# 작성자 : 한동근

import random

string_list = [
    ["나는","학교를","간다"],
    ["당신은","부채를","가졌다"],
    ["집으로","가는길이","힘겹다"],
    ["입장을","바꾸어서","생각하다"],
    ["누구나","계획을","가진다"],
    ["맛있는","갈치를","먹다"],
    ["시장에는","반찬을","판다"],
    ["멋진","코딩을","짜다"],
]

game_count = 5 # 총 게임횟수
score = 0

for i in range(game_count):
    print() # 다음 문장
    sel_string = random.choice(string_list) # 랜덤 문장 선택
    out_string = sel_string[0]+" "+sel_string[1]+" "+sel_string[2] # 랜덤 문장내 리스트를 문자열로 변환
    random_string = random.sample(sel_string,3) # 랜덤 문장 내 문자열 섞기
    print("제시문장 :", end=' ')
    for j in random_string:
        print(j, end = " ")
    user_string = input("\n입    력 : ")
    if user_string == out_string:
        print("올바른 문장입니다.\n")
        score += 1
    else:
        print(f"바른문장 : {out_string}.\n")

print()
print(f"게임 시도 횟수 {game_count} 회중 성공횟수는 {score} 입니다.")