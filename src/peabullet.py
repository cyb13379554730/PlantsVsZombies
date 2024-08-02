#豌豆射手子弹的类
from src import objectbase

class Peabullet(objectbase.ObjectBase):

    def __init__(self, pathFmt, pathIndex, pos, size=None, pathIndexCount=0):
        super().__init__(pathFmt, pathIndex, pos, size, pathIndexCount)

    def getProcessionCD(self):
        return 0.006
    def checkPostion(self):
        b = super(Peabullet,self).checkPostion()
        if b:
            self.doRight()
        return b