def move(data, xoffset, yoffset):
    data['xpos'] += xoffset
    data['ypos'] += yoffset

def get_point(data, offset):
    data['point'] += offset
    
def update_energy(data, offset):
    data['energy'] += offset


mario = {'xpos':10, 'ypos':0, 'point':0, 'energy':100}    
mario2 ={'xpos':10, 'ypos':0, 'point':0, 'energy':100}

    
move(mario, 20, 0)
move(mario2, 30, 0)   


print("mario 1P",mario['xpos'], mario['ypos']) 
print("mario 2P",mario2['xpos'], mario2['ypos']) 

    
       
    
    
    
    