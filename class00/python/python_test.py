#변창섭
import random
choice=[]
ranran_list=[]
My_list=[["나는","학교에","간다"],["내일은","수요일","입니다"],["5시에","수업이","끝납니다"],["나는","머리가","아픕니다"]
,["집에서","치킨을","먹습니다"],["목요일은","방학","입니다"],["오늘의","수업은","여기까지"]]
for i in range(5):
    ran_list=random.choice(My_list)
    for j in range(len(ran_list)):
        choice=(random.choice(ran_list))
        ranran_list.append(choice)
        ran_list.remove(choice)
    print(f"{ranran_list[0]} {ranran_list[1]} {ranran_list[2]}")
    sum=ranran_list[0]+" "+{ranran_list[1]}+" "+ ranran_list[2]
    ans=input("다음 단어를 올바른 순서로 입력하시오: ")
    if(ans==sum):
        print("정답입니다!")
    else:
        print("틀렸습니다!")