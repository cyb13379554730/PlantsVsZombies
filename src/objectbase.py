#所有对象的基类 向日葵、子弹、阳光等都继承这个类
import time

import image

class ObjectBase(image.Image):
    def __init__(self, pathFmt, pathIndex, pos, size=None, pathIndexCount=0):
        super(ObjectBase,self).__init__(pathFmt, pathIndex, pos, size, pathIndexCount)
        self.preIndexTime = 0
        self.prePositionTime = 0

    def update(self):
        self.checkImageIndex()
        self.checkPostion()

    #帧动画
    def checkImageIndex(self):
        if time.time() - self.preIndexTime <= 0.2:
            return
        self.preIndexTime = time.time()
        idx = self.pathIndex + 1
        if idx >= self.pathIndexCount:
            idx = 0
        self.updateIndex(idx)

    #平移动画
    def checkPostion(self):
        if time.time() - self.prePositionTime <= 0.2:
            return False
        self.prePositionTime = time.time()
        return True
        #植物不会移动，所以要让会移动的子类，实现这个功能.所以在这里让这个方法return一个布尔值
        #self.pos[0] -= 2.5

