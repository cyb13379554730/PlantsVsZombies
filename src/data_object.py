#表文件,存储僵尸、植物等元素的信息数据，其主要是字典

#0是豌豆射手的子弹
# 1是僵尸
# 2是阳光
data = {
    0:{
        "PATH" : "../imageresources/other/peabullet.png",
        "IMAGE_INDEX_MAX" : 0,
        "IMAGE_INDEX_CD" : 0.0,
        "POSSION_CD" : 0.006,
        "SIZE" : (25,25)
    },

    1:{
        "PATH" : "../imageresources/zombie/0/%d.png",
        "IMAGE_INDEX_MAX" : 15,
        "IMAGE_INDEX_CD" : 0.2,
        "POSSION_CD" : 0.2,
        "SIZE" : (100,128)
    },

    2:{
        "PATH" : "../imageresources/other/sunlight/%d.png",
        "IMAGE_INDEX_MAX" : 30,
        "IMAGE_INDEX_CD" : 0.2,
        "POSSION_CD" : 0.2,
        "SIZE" : (300,300)
    }
}