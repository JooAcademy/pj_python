# -*- coding: utf-8 -*-
# for 문과 dictionary

과자 = {
     "꼬깔콘" : 2000,
     "맛동산" : 4990,
     "포카칩" : 3500    
     }

for i in 과자:
    print(i)


for i in 과자:
    print(i, 과자[i])

for k, v in 과자.items():
    print(k, v)




