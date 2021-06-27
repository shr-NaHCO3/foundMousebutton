import math
import random









def omap(screenLong,screenWide,squareLong,isKeyMap):
    '''
    omap : output a map
    参数：
        screenLong : 电脑屏幕的长
        screenWide : 电脑屏幕的宽
        squareLong : 网格的边长
        isKeyMap : 是否为中心地图。如是，地图中心及周围边上的中点将被设为畅通。
    
    输出：
        包括一个数组。0表示畅通，1表示障碍
    ''' 
    X = math.floor(screenLong/squareLong)#沿着长边能铺几个网格
    Y = math.floor(screenWide/squareLong)#沿着宽边能铺几个网格
    mapp = [ [1 for j in range(X)] for i in range(Y)] #形成初步地图

    X = X-1 #减一，便于以后的逻辑思考和调用方便。
    Y = Y-1 #减一，便于以后的逻辑思考和调用方便。

    a_1 = False #(0   , x/2)
    a_2 = False #(y/2 ,   0)
    a_3 = False #(y   , x/2)
    a_4 = False #(y/2 ,   x)

    #将必要的地方设为畅通
    mapp[math.floor(Y/2)][math.floor(X/2)] = 0
    mapp[0][math.floor(X/2)] = 0
    mapp[math.floor(Y/2)][0] = 0
    mapp[Y][math.floor(X/2)] = 0
    mapp[math.floor(Y/2)][X] = 0
    
    #检测是否为keymap,
    if isKeyMap :
        a_1 = a_2 = a_3 = a_4 = True
    else:
        a_1 = bool(random.randint(0,1))
    
    
    #路径形成
    #上 - 中（a_1）
    if a_1:
        x = math.floor(X/2)
        y = math.floor(Y/2)
        for i in range(math.floor(Y/2) - int(Y%2)):
            x += random.randint(-1,1)
            mapp[y][x] = 0
            mapp[y-1][x] = 0
            y -= 1
        while y > 0:
            y-=1
            mapp[y][x] = 0
        while x != math.floor(X/2):
            if x < math.floor(X/2):
                x += 1
            else:
                x -= 1
            mapp[y][x] = 0
    
    #左 - 中（a_2）
    if a_2:
        x = math.floor(X/2)
        y = math.floor(Y/2)
        for i in range(math.floor(X/2) - int(X%2)):
            y += random.randint(-1,1)
            mapp[y][x] = 0
            mapp[y][x-1] = 0
            x -= 1
        while x > 0:
            x -= 1
            mapp[y][x] = 0
        while y != math.floor(Y/2):
            if y < math.floor(Y/2):
                y += 1
            else:
                y -= 1
            mapp[y][x] = 0

    #下 - 中（a_3）
    if a_1:
        x = math.floor(X/2)
        y = math.floor(Y/2)
        for i in range(math.floor(Y/2) + int(Y%2)):
            x += random.randint(-1,1)
            mapp[y][x] = 0
            mapp[y+1][x] = 0
            y += 1
        while y < Y:
            y += 1
            mapp[y][x] = 0
        while x != math.floor(X/2):
            if x < math.floor(X/2):
                x += 1
            else:
                x -= 1
            mapp[y][x] = 0
    
    #右 - 中（a_4）
    if a_2:
        x = math.floor(X/2)
        y = math.floor(Y/2)
        for i in range(math.floor(X/2) - int(X%2)):
            y += random.randint(-1,1)
            mapp[y][x] = 0
            mapp[y][x+1] = 0
            x += 1
        while x < X:
            x += 1
            mapp[y][x] = 0
        while y != math.floor(Y/2):
            if y < math.floor(Y/2):
                y += 1
            else:
                y -= 1
            mapp[y][x] = 0

    return mapp

