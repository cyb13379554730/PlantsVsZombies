import sys

import pygame
from pygame.locals import *

#初始化一个pygame模块
pygame.init()

#创建一个窗口，并设置尺寸
DS = pygame.display.set_mode(size=(1280,600))

#用来加载图片
#image = pygame.image.load("图片路径")

#这里设置循环，是防止主程序直接运行完退出
while 1:
    for event in pygame.event.get():
        #QUIT是from pygame.locals import *库中的一个状态
        if event == QUIT:
            #退出pygame
            pygame.quit()
            sys.exit()
            #设置颜色，分别是红色、绿色、蓝色。最大值是255，设置未0则不显示那个颜色，全255是白色
    DS.fill((255,255,255))
    pygame.display.update()

