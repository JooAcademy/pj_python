### 유튜버 주간컴공 지마&참깨의 프리패스 파이썬 
### 8장 3. 클래스 실습


'''
메소드 중 생성자의 역할을 하는 메소드가 있습니다.
생성자는 객체가 생성될 때, 단 한 번만 자동으로 호출 되는 메소드
'''

class Knight:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.mp = 20
        self.attack_type = "근접"
        self.attack = 30
        self.armor = 10
        self.potion_cnt = 3
        
    # 피격 사망 메소드
    def under_attack(self, attacker):
        #공격 타입이 마법일 경우엔 20% 데미지 가중
        if attacker.attack_type == "마법":
            multiple = 1.2
        else:
            multiple = 1.0
            
        # 공격력 * 가중치 - 방어력
        damage = attacker.attack * multiple - self.armor
        self.hp -= damage
        #print("{0}:{1}님의 공격({2})에 의해 HP[{3}]".format(self.name, attacker.name, damage, self.hp))
        print(f"{self.name}:{attacker.name}님의 공격({damage})에 의해 HP[{self.hp}]")
        
        # 체력이 0이 된 경우, 사망 메시지 출력
        if self.hp <= 0:
            print("{0}님이 {1}님에 의해 사망했습니다. ".format(self.name, attacker.name))
            
    # 공격메소드
    def attack_to(self, target):
        #공격 대상의 체력이 0 이상일 때만 실행
        if target.hp > 0:
            print("{0}님이 {1}님을 공격합니다.".format(self.name, target.name))
            
            # 공격 대상의 피격 메소드 호출
            target.under_attack(self)
    
    # 특수공격 메소드
    def triple_attack(self, target):
        # mp가 20 이상일 때만 사용 가능
        if self. mp >= 20:
            self.mp -= 20
            print("{0}님이 {1}님을 3회 공격합니다. ".format(self.name, target.name))
            # 공격 대상의 under_attack 메소드 3회 호출
            for i in range(3):
                target.under_attack(self)
                
                
k1 = Knight("길동")
k2 = Knight("철수")

k1.attack_to(k2)                
k1.attack_to(k2)
k2.attack_to(k1)
k1.triple_attack(k2)
k1.attack_to(k2)
        

