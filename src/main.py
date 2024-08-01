import sys

import pygame
from pygame.locals import *

from src.const import *

#初始化一个pygame模块
pygame.init()

#创建一个窗口，并设置尺寸
DS = pygame.display.set_mode(size=GAME_SIZE)

#用来加载图片
#image = pygame.image.load("../imageresources/other/back.png")
import image
#背景图
backgroundImage = image.Image(PTAT_BACK,0,(0,0),GAME_SIZE)
#僵尸
zombieImage = image.Image("../imageresources/zombie/0/%d.png",0,(1280,200),(100,128),15)

#这里设置循环，是防止主程序直接运行完退出
while 1:
    for event in pygame.event.get():
        #QUIT是from pygame.locals import *库中的一个状态
        if event.type == QUIT:
            #退出pygame
            pygame.quit()
            sys.exit()
    #设置颜色，分别是红色、绿色、蓝色。最大值是255，设置未0则不显示那个颜色，全255是白色
    DS.fill((255,255,255))

    #将背景图片显示出来,第一个参数是图片，第二个参数获取的是图片的矩形
    #DS.blit(image,image.get_rect())
    backgroundImage.draw(DS)

    zombieImage.draw(DS)
    zombieImage.doLeft()
    zombieImage.updateIndex((zombieImage.pathIndex+1) % 15)

    pygame.display.update()

