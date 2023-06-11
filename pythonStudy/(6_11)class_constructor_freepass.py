### 유튜버 주간컴공 지마&참깨의 프리패스 파이썬 
### 8장 1. 클래스 self


'''
클래스는 자료구조(속성)와 이것을 제어할 수 있는 메소드
때문에 메소드밖에 있는 멤버들에 접근할 수단이 필요한데, 이것이 바로 self
'''

class ClassicCar:
    def __init__(self, color): #생성자 메소드
        # 클래스 변스 color에 매개변수 color 할당
        self.color = color
        
    def test(self): # self를 안쓰면 에러
        print("self.color =", self.color)
        

father = ClassicCar("빨간색")
father.test() #객체 자신을 인수로 넘겨주고 있음
father.color ="검정색"
father.test()

