import pygame
import random

# 초기화
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Typing Game!")
FONT = pygame.font.SysFont("malgun gothic", 48)
INPUT_FONT = pygame.font.SysFont("malgun gothic", 36)
TIMER = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER, 2000)
clock = pygame.time.Clock()

# 단어 리스트
# To Do List:
# 영어 단어들로만 구성된 List 생성
WORDS = []
    
# 게임 상태 변수
user_input = ""
score = 0
lives = 3
falling_words = []

def get_random_word():
    # To Do List:
    # 랜덤 단어를 반환하는 함수
    # 이 함수는 단어 리스트에서 무작위로 단어를 선택하여 반환합니다.

def add_falling_word():
    # To Do List:
    # 떨어지는 단어를 추가하는 함수
    # 이 함수는 get_random_word() 함수를 호출하여 단어를 가져오고,
    # 해당 단어의 위치와 속도를 설정하여 falling_words 리스트에 추가합니다.
    # word =  # 랜덤 단어
    # x =     # 랜덤 x 좌표 (50에서 700 사이)
    # y =     # 랜덤 y 좌표 (시작 위치는 화면 상단)
    # speed = # 랜덤 속도 (2에서 5 사이)
    # falling_words # 리스트에 추가 (word, x, y, speed)

def update_words():
    # To Do List:
    # 떨어지는 단어들의 위치를 업데이트하는 함수
    # 이 함수는 falling_words 리스트의 각 단어에 대해 y 좌표를 speed만큼 증가시킵니다.

def check_input():
    # To Do List:
    # 사용자가 입력한 단어가 떨어지는 단어와 일치하는지 확인하는 함수
    # 이 함수는 falling_words 리스트를 순회하며 user_input과 일치하는 단어를 찾습니다.
    # 일치하는 단어가 있으면 
    #         - 해당 단어를 falling_words에서 제거하고,
    #         - 점수를 10점 증가시키고 user_input을 초기화합니다.
    # 일치하는 단어가 없으면 
    #         - user_input을 초기화합니다.
    # 반환은 True 또는 False로, 일치하는 단어가 있었는지 여부를 나타냅니다.

def check_missed():
    # To Do List:
    # 떨어지는 단어가 화면 아래로 넘어갔는지 확인하는 함수
    # 이 함수는 falling_words 리스트를 순회하며 y 좌표가 600을 초과하는 단어를 찾습니다.
    # 해당 단어를 falling_words에서 제거하고 lives를 1 감소시킵니다.

def draw_words():
    for word in falling_words:
        text = FONT.render(word["word"], True, (255, 255, 255))
        screen.blit(text, (word["x"], word["y"]))

def draw_ui():
    draw_words()
    input_text = INPUT_FONT.render(f"입력: {user_input}", True, (0, 255, 0))
    score_text = INPUT_FONT.render(f"점수: {score}", True, (255, 255, 0))
    lives_text = INPUT_FONT.render(f"목숨: {lives}", True, (255, 100, 100))
    screen.blit(input_text, (20, 550))
    screen.blit(score_text, (650, 20))
    screen.blit(lives_text, (650, 60))

# 메인 루프
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == TIMER:
            add_falling_word()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            elif event.key == pygame.K_RETURN:
                check_input()
            else:
                user_input += event.unicode

    update_words()
    check_missed()
    draw_ui()

    if lives <= 0:
        game_over_text = FONT.render("Game Over", True, (255, 0, 0))
        screen.blit(game_over_text, (300, 250))
        pygame.display.update()
        pygame.time.wait(3000)
        running = False

    pygame.display.update()
    clock.tick(30)

pygame.quit()
