import sys

import pygame
from pygame.locals import *

from src import peabullet
from src.const import *
import zombiebase
import sunlight
#初始化一个pygame模块
pygame.init()

#创建一个窗口，并设置尺寸
DS = pygame.display.set_mode(size=GAME_SIZE)

#用来加载图片
#backgroundImage = pygame.image.load("../imageresources/other/back.png")
import image
#背景图
backgroundImage = image.Image(PTAT_BACK,0,(0,0),GAME_SIZE)
#僵尸
zombieImage = zombiebase.ZombieBase(1,(1100,200))
#阳光
sunlight = sunlight.SunLight(2,(250,200))

#豌豆子弹
peabul = peabullet.Peabullet(0,(300,250))

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

    #将背景图片显示出来,第一个参数是图片，第二个参数是绘制的位置坐标
    #DS.blit(backgroundImage,backgroundImage.get_rect())
    backgroundImage.draw(DS)

    zombieImage.update()
    zombieImage.draw(DS)

    peabul.update()
    peabul.draw(DS)

    sunlight.update()
    sunlight.draw(DS)

    pygame.display.update()

