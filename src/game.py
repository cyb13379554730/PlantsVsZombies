#用于实现游戏的主要逻辑
from src import image
from src.const import *
import sunflower

class Game(object):
    def __init__(self,ds):
        self.ds = ds
        self.back = image.Image(PTAT_BACK,0,(0,0),GAME_SIZE)
        self.plants = []
        self.summons = []

        for i in range(GRID_COUNT[0]):
            for j in range(GRID_COUNT[1]):
                posX = LEFT_TOP[0] + i * GRID_SIZE[0]
                posY = LEFT_TOP[1] + j * GRID_SIZE[1]
                pos = posX, posY

                sunflower1 = sunflower.SunFlower(3, pos)
                self.plants.append(sunflower1)

    def draw(self):
        self.back.draw(self.ds)
        for plant in self.plants:
            plant.draw(self.ds)
        for summon in self.summons:
            summon.draw(self.ds)

    def update(self):
        self.back.update()
        for plant in self.plants:
            plant.update()
            #判断当前植物身上是否有召唤物，如过有，先不要创建，等待调用doSummon后再创建。
            if plant.hasSummon():
                summ = plant.doSummon()
                # 创建好之后放在summons列表由当前背景保管，而不是植物再去保管
                self.summons.append(summ)
        for summon in self.summons:
            summon.update()

