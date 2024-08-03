#所有对象的基类 向日葵、子弹、阳光等都继承这个类
import time

import image
import data_object

class ObjectBase(image.Image):
    def __init__(self,id,pos):
        self.id = id
        self.preIndexTime = 0
        self.prePositionTime = 0
        self.preSumTime = 0
        super(ObjectBase,self).__init__(self.getDataSelf()["PATH"],
                                        0,
                                        pos,
                                        self.getDataSelf()["SIZE"],
                                        self.getDataSelf()["IMAGE_INDEX_MAX"])

    def getDataSelf(self):
        return data_object.data[self.id]

    def getSpeed(self):
        return self.getDataSelf()["SPEED"]

    def getPreSumTimeCD(self):
        return self.getDataSelf()["SUMMON_CD"]

    def checkSummon(self):
        if time.time() - self.preSumTime <= self.getPreSumTimeCD() or self.getPreSumTimeCD() == -1:
            return
        self.preSumTime = time.time()
        self.preSummon()

    #这个函数用来让向日葵生产阳光
    def preSummon(self):
        pass

    def hasSummon(self):
        pass

    def doSummon(self):
        pass

    def update(self):
        self.checkImageIndex()
        self.checkPostion()
        self.checkSummon()

    #根据此函数判断平移动画切换的时间,子类去实现，赋予返回值
    def getProcessionCD(self):
        return self.getDataSelf()["POSSION_CD"]

    #控制帧动画每/s切换一次图片
    def getImageIndex(self):
        return self.getDataSelf()["IMAGE_INDEX_CD"]

    #帧动画
    def checkImageIndex(self):
        if time.time() - self.preIndexTime <= self.getImageIndex():
            return
        self.preIndexTime = time.time()
        idx = self.pathIndex + 1
        if idx >= self.pathIndexCount:
            idx = 0
        self.updateIndex(idx)

    #平移动画
    def checkPostion(self):
        if time.time() - self.prePositionTime <= self.getProcessionCD():
            return False
        self.prePositionTime = time.time()
        speed = self.getSpeed()
        self.pos = (self.pos[0] + speed[0], self.pos[1] + speed[1])
        return True
        #植物不会移动，所以要让会移动的子类，实现这个功能.所以在这里让这个方法return一个布尔值
        #self.pos[0] -= 2.5

