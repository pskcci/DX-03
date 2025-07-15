import random

list_a = [["나는", "학교를", "간다"], ["나는", "늦게", "달린다"],["오늘","학교를","쨋다"],["나는","학원을","쨋다"]]

def random_choice():
    return random.choice(list_a)

def print_mix_list(sentence):
    mixed = sentence.copy()
    random.shuffle(mixed)
    print("섞인 단어:", mixed)
    return mixed

def user_input_list():
    return input("입력하세요: ").split()

answer = 0

for _ in range(5):
    correct_list = random_choice()
    print_mix_list(correct_list)
    user_input = user_input_list()

    if user_input == correct_list:
        print("정답")
        answer += 1
    else:
        print("실패")
        print("정답은:", " ".join(correct_list))

print(f"맞춘 수: {answer}")
print("Su go!")
