#僵尸的基类

import objectbase

class ZombieBase(objectbase.ObjectBase):
    def __init__(self, id,pos):
        super(ZombieBase,self).__init__(id,pos)

    def checkPostion(self):
        b = super(ZombieBase,self).checkPostion()
        if b:
            self.pos[0] -= 2.5
        return b