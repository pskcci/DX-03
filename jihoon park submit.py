import random

def create_sentence_game():
    sentences = [
        ["나는", "학교를", "간다"],
        ["엄마가", "요리를", "한다"],
        ["친구가", "책을", "읽는다"],
        ["동생이", "게임을", "한다"],
        ["아빠가", "운동을", "한다"]
    ]

    successful_attempts = 0
    total_rounds = 5

    print("올바른 한글 문장 만들기 게임 시작!\n")
    print("제시된 단어들을 사용하여 올바른 문장을 만드세요.\n")

    for i in range(total_rounds):
        print(f"===라운드 {i + 1}/{total_rounds} ---")

        correct_sentence_list = random.choice(sentences)
        correct_sentence_str = " ".join(correct_sentence_list)

        shuffled_words = random.sample(correct_sentence_list, len(correct_sentence_list))
        shuffled_question = " ".join(shuffled_words) + "?"
        print(f"제시된 단어: {shuffled_question}")

        # 게임 유저가 올바른 문장으로 만들어서 입력 
        user_input = input("올바른 문장을 입력하세요: ").strip()

        # 맞았는지 틀리는지 출력 
        if user_input == correct_sentence_str:
            print("정답입니다!\n")
            successful_attempts += 1
        else:
            print(f"틀렸습니다. 정답은 '{correct_sentence_str}' 입니다.\n")

    print(f"--- 게임 종료 ---")
    print(f"총 5회 게임 중 {successful_attempts}회 성공했습니다.")
    print("수고하셨습니다!")

# 게임 실행
if __name__ == "__main__":
    create_sentence_game()