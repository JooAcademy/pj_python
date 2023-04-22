# -*- coding: utf-8 -*-
# 문자열 포맷 format 함수

name ="철수"
score = 290
average = 290/3


print("%s의 총점은 %d, 평균은 %f입니다. " %(name, score, average))

print("{}의 총점은 {}, 평균은 {}입니다. " .format(name, score, average))

print(f"{name}의 총점은 {score}, 평균은 {average}입니다.")



coin_price = 128000000
print(f"코인 가격:{coin_price}")
print(f"코인 가격:{coin_price: 10>,}")   # 10>, 는 숫자를 우측정렬하고 천단위 콤마(,)찍기