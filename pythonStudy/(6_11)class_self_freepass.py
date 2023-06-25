### 유튜버 주간컴공 지마&참깨의 프리패스 파이썬 
### 8장 2. 클래스 self


'''
객체를 통해서 호출하는 메소드는 기본적으로 자기 자신이 인수로 지정됩니다.
'''

class ClassicCar:
    def drive(self): # self를 안쓰면 에러
        print("수동 운전 모드")

father = ClassicCar()
father.drive() #객체 자신을 인수로 넘겨주고 있음



