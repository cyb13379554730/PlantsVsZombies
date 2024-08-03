#表文件,存储僵尸、植物等元素的信息数据，其主要是字典

#0是豌豆射手的子弹
# 1是僵尸
# 2是阳光
# 3是向日葵
data = {
    0:{
        "PATH" : "../imageresources/other/peabullet.png",
        "SIZE" : (25,25),
        "IMAGE_INDEX_MAX" : 0,
        "IMAGE_INDEX_CD" : 0.0,
        "POSSION_CD" : 0.006,
        "SUMMON_CD" : -1,
        "SPEED" : (2.5,0)
    },

    1:{
        "PATH" : "../imageresources/zombie/0/%d.png",
        "IMAGE_INDEX_MAX" : 15,
        "SIZE" : (100,128),
        "IMAGE_INDEX_CD" : 0.2,
        "POSSION_CD" : 0.2,
        "SUMMON_CD" : -1,
        "SPEED" : (-2.5,0)
    },

    2:{
        "PATH" : "../imageresources/other/sunlight/%d.png",
        "SIZE" : (80,80),
        "IMAGE_INDEX_MAX" : 30,
        "IMAGE_INDEX_CD" : 0.03,
        "POSSION_CD" : 0.08,
        "SUMMON_CD" : -1,
        "SPEED" : (0,2)
    },

    3:{
        "PATH" : "../imageresources/plant/sunflower/%d.png",
        "SIZE" : (130,130),
        "IMAGE_INDEX_MAX" : 19,
        "IMAGE_INDEX_CD" : 0.08,
        "POSSION_CD" : 0,
        "SUMMON_CD" : 8,
        "SPEED" : (0,0)
    }

}