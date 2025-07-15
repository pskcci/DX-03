# 작성자 : 박우현

import random

list1 = [[["나는"],["학교를"],["간다"]],
         [["저녁에"],["밥을"],["먹는다"]],
         [["오늘도"],["출근을"],["한다"]],
         [["주말에"],["여행을"],["간다"]],
         [["내일은"],["아무것도"],["안한다"]]]

for i in range(1,6):
  print(f"문제 {i} : ")
  print("다음 단어들을 올바른 순서로 조합하세요 : ")
  list2 = random.choice(list1)
  front = str(" ".join(list2[0]))
  middle = str(" ".join(list2[1]))
  back = str(" ".join(list2[2]))
  list3 = [front,middle,back]
  random.shuffle(list3)
  print(" ".join(list3))
  
  a = front,middle,back
  b = (" ".join(a))

  answer = input(f"정확한 문장을 입력하세요 : {list3}")
  print(f"정확한 문장을 입력하세요 : {answer}")
  
  if answer == b:
    print("정답입니다!")
  else:
    print("오답입니다!")