#向日葵的类

import objectbase
import sunlight

class SunFlower(objectbase.ObjectBase):

    def __init__(self, id, pos):
        super(SunFlower,self).__init__(id, pos)
        self.hasSumLight = False

    #判断是否需要去召唤召唤物，需要的话就把hasSumLight置为true
    def preSummon(self):
        self.hasSumLight = True

    def hasSummon(self):
        return self.hasSumLight

    def doSummon(self):
        #判断是否要返回召唤物对象
        if self.hasSummon():
            self.hasSumLight = False
            return sunlight.SunLight(2, (self.pos[0]+20,self.pos[1]-5))






