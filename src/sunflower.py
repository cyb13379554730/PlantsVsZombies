#向日葵的类

import objectbase
import sunlight

class SunFlower(objectbase.ObjectBase):

    def __init__(self, id, pos):
        super(SunFlower,self).__init__(id, pos)
        #初始化向日葵时，记录下来有多少个阳光
        self.sunlightList = []

    #这个函数用来让向日葵生产阳光
    def preSummon(self):
        # 阳光
        # 阳光产生的位置和向日葵是相近的，所以用向日葵的位置计算阳光产生的位置
        sunlight1 = sunlight.SunLight(2, (self.pos[0]+20,self.pos[1]-5))
        self.sunlightList.append(sunlight1)

    def update(self):
        super().update()
        for sl in self.sunlightList:
            sl.update()

    def draw(self, ds):
        super().draw(ds)
        for sl in self.sunlightList:
            sl.draw(ds)




