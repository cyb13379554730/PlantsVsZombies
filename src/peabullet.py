#豌豆射手子弹的类
from src import objectbase

class Peabullet(objectbase.ObjectBase):

    def __init__(self ,id,pos):
        super().__init__(id,pos)

    def checkPostion(self):
        b = super(Peabullet,self).checkPostion()
        if b:
            self.doRight()
        return b