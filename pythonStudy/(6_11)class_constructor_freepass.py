### 유튜버 주간컴공 지마&참깨의 프리패스 파이썬 
### 8장 2. 클래스 생성자 메소드 


'''
메소드 중 생성자의 역할을 하는 메소드가 있습니다.
생성자는 객체가 생성될 때, 단 한 번만 자동으로 호출 되는 메소드
'''

class ClassicCar:
    def __init__(self, color): #생성자 메소드
        # 클래스 변스 color에 매개변수 color 할당
        self.color = color
        
    def test(self): # self를 안쓰면 에러
        print("self.color =", self.color)
        

father = ClassicCar("빨간색")
father.test() #객체 자신을 인수로 넘겨주고 있음
father.color ="파란색"
father.test()

