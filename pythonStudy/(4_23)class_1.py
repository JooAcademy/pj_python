### 북수원 도서관 그림으로 배우는 파이썬 기초문법 ###

"""
mario = {'xpos':10, 'ypos':0, 'point':0, 'energy':100}

def move(data, xoffset, yoffset):
    data['xpos'] += xoffset
    data['ypos'] += yoffset
    
def get_point(data, offset):
    data['point'] += offset
    
def update_energy(data, offset):
    data['energy'] += offset
    
mario2 ={'xpos':10, 'ypos':0, 'point':0, 'energy':100}
    
move(mario, 20, 0)
move(mario2, 30, 0)   
print("mario 1P",mario['xpos'], mario['ypos']) 
print("mario 2P",mario2['xpos'], mario2['ypos']) 
"""

class SuperMario:
    def __init__(self):
        self.xpos = 10
        self.ypos = 0
        
    def move(self, xoffset, yoffset):
        self.xpos += xoffset
        self.ypos += yoffset
    
mario_1p = SuperMario()  
mario_2p = SuperMario()       

mario_1p.move(20, 0)
mario_2p.move(30, 0)   

print("mario 1P", mario_1p.xpos, mario_1p.ypos) 
print("mario 2P", mario_2p.xpos, mario_2p.ypos) 
    
 