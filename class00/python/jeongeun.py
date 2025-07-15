
import random

# 3단어 구성된 올바른 문장 3개
subjects = ["나는","너는","학생은"]
objects = ["학교를","밥을","책을"]
verbs = ["간다","먹는다","읽는다"]

# 정답 리스트 생성
correct_sentences = [
    f"{subjects[0]} {objects[0]} {verbs[0]}", # 나는 학교를 간다
    f"{subjects[1]} {objects[1]} {verbs[1]}", #너는 밥을 먹는다
    f"{subjects[2]} {objects[2]} {verbs[2]}" # 학생은 책을 읽는다
]

score = 0
total_rounds = 5

print("올바른 한글 문장 만들기 게임 시작!\n")

for round_num in range(1, total_rounds + 1):
# 부작위로 하나의 문장을 선택
idx = random.randint(0,2)
chosen_subject = subjects[idx]
chosen_object = objects[idx]
chosen_verb = verbs[idx]

# 단어 섞기
words = [chosen_subject, chosen_object, chosen_verb]
random.shuffle(words)

print(f"\n 문제 {round_num}: 다음 단어로 올바른 문장을 입력하세요.")
print("단어:",",".join(words))

user_import = input("입력: ").strip()

correct_answer = f"{chosen_subject} {chosen_object} {chosen_verb}"

if user_input == correct_answer:
    print("정답입니다!")
    score += 1
else:
    print("틀렸습니다.")
    print(f"정답은: {correct_answer}")
print(f"\n 게임 종료! 총 {score}문제 맞췄습니다.")