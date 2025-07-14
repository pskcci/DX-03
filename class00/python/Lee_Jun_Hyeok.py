import random

sentences = [["나는", "학교를", "간다"], ["나는", "회사를", "갔다"], ["나는", "미술관을", "갔나?"], ["나는", "영화관을", "갔거나"], ["나는", "학교를", "가지 않았다"], 
             ["당신은", "사람", "일수도"],["당신은", "수영장을", "간다"],["당신은", "도서관을", "갔지?"],["당신은", "체육관을", "가버렸다"]
            ]

user_try = 0 
num_rounds = 5       

print("--- 단어 조합 게임을 시작합니다! ---")
print(f"총 {num_rounds}회 진행됩니다.")


for i in range(1, num_rounds + 1):
    print(f"\n {i}번째 문제")
       
    r_sentences = random.choice(sentences)
        
    correct_answer_string = " ".join(r_sentences)

       
    rr_sentences = r_sentences[:] 
    random.shuffle(rr_sentences) 
        
    user_input = input(f"단어들을 보고 올바른 문장으로 조합하세요: {rr_sentences}\n당신의 답변: ")
    
   
    if user_input.strip() == correct_answer_string.strip():
        print(" 맞았습니다! ")
        correct_attempts += 1 
    else:
        print(f"틀렸습니다. 정답은 '{correct_answer_string}' 입니다.")

print("\n--- 게임 종료 ---")
print(f"총 {num_rounds}회 중 {user_try}회 성공하셨습니다.")
print("다음에 또 만나요!")