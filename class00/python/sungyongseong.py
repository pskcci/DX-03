# 작성자: 성승용

import random

star = [["철수는","학교를","간다"],["영희는","수퍼에","간다"]["민수는","애견샆에","간다"],["동수는","운동하려","간다"],["둘리는","비자루를","탄다"],["철이는","기차를","탄다"]]
def make_sentence():
    star = random.choice(star)
    return f"{star}"
if __name__ == "__main__":
    print("올바른 한문장 만들기 프로그램!")
    count = int(input("몇 개의 문장을 생성 할까요 >> "))
    sentences = [make_sentence() for in range(count)]
    
    print("\n[생성된 문장들]")
    for s in sentences:
        print(s)

    with open("sentences.txt,"w",encoding = "utf-8 as f: )
                                          for s in sentences:
                                              f.write(s + "\n")
                                    print("\n sentences.txt 파일에 저장되었습니다")
                                         