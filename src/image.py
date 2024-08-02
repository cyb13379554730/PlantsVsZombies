#实现图片的类

import pygame

class Image(pygame.sprite.Sprite):
    def __init__(self, pathFmt,pathIndex,pos,size=None,pathIndexCount=0):
        self.pathFmt = pathFmt
        self.pathIndex = pathIndex
        self.pathIndexCount = pathIndexCount
        self.size = size
        #坐标信息
        self.pos = list(pos)
        self.updateImage()

    def updateImage(self):
        path = self.pathFmt
        if self.pathIndexCount != 0:
            #通过对路径字符串的格式化拼接，实现图片不停切换
            path = path % self.pathIndex
        # 表示在初始化image时候就会开始加载图片了，将这个方法封装了起来
        self.image = pygame.image.load(path)
        if self.size:
            # 实现图片缩放 pygame.transform.scale实际是将图片裁剪后又返回了一个裁剪后的img，所以又赋值给image
            self.image = pygame.transform.scale(self.image, self.size)

    def updateSize(self,size):
        self.size = size
        self.updateImage()

    def updateIndex(self,pathIndex):
        self.pathIndex = pathIndex
        self.updateImage()

    def getRect(self):
        #获取到整个图片的矩形，这个矩形有一个坐标分别是x和y，控制着图片在左上角的哪个位置,返回值就是xy
        rect = self.image.get_rect()
        #通过实例化img传过来的pos，分别给xy坐标赋值，控制图片的位置
        rect.x = self.pos[0]
        rect.y = self.pos[1]
        return rect

    # #这个函数控制僵尸从右往左走，所以是x坐标每次-1，但因为传过来的是一个元组，元组不可改变，所以在init中，将pos类型转为list
    # def doLeft(self):
    #     self.pos[0] -= 2.5
    #
    # def doRight(self):
    #     self.pos[0] += 2.5

    def draw(self,ds):
        ds.blit(self.image,self.getRect())



