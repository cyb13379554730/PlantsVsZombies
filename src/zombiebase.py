#僵尸的基类

import objectbase

class ZombieBase(objectbase.ObjectBase):
    def __init__(self, pathFmt, pathIndex, pos, size=None, pathIndexCount=0):
        super(ZombieBase,self).__init__(pathFmt, pathIndex, pos, size, pathIndexCount)

    def checkPostion(self):
        b = super(ZombieBase,self).checkPostion()
        if b:
            self.pos[0] -= 2.5
        return b