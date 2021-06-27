try:
    import pygame as pg
    import math
    import random
    import omap



    #--- init ---#
    pg.init()
    root = pg.display.set_mode([1000,700])#窗口大小
    pg.display.set_caption("FOUND MOUSEBUTTON - 0.0.1 (0.0.0.0)")#title
    pg_timer = pg.time.Clock()#时钟对象



    #--- colors ---#
    WHITE = (255,255,255)
    RED = (155,0,0)
    GREEN = (0,255,0)
    BLUE = (0,133,200)
    BLACK = (0,0,0)
    MAINGREY = (30,30,30)



    #--- fill and update ---#
    root.fill(MAINGREY)
    pg.display.update()



    #--- fonts ---#
    CH = pg.font.Font('ch.ttf', 43)
    EN = pg.font.Font('en.ttf', 43)



    #--- unknows ---#
    time = 0
    running_course = 0 #运行的进程


    #---  pictures  ---#
    picture_mainButton = pg.image.load("main.png") #150*80
    picture_mouseButton = pg.image.load("mousebutton.png") #50*79



    #--- functions ---#
    def textOut(text,color,font=EN):
        '''
        # 生成pygame字符对象

        参数：
            text:字符
            color:颜色
            *font:字体，默认EN

        输出：pygame字符对象
        '''
        return font.render(text,True,color)


    def rot_center(image, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = image.get_rect()
        rot_image = pg.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image


    picture_mouseButton = rot_center(picture_mouseButton,30)


    Map = {
        0 : {
            0 : omap.omap(900,700,50,True)
        }
    }
    player_zone = [0,0]
    playerx = 8
    playery = 6

    mapSurface = pg.Surface([900,700])
    pg.draw.rect(mapSurface, WHITE, (0,0,900,700), 0)
    for i in range(18): #行
        for j in range(14): #列
            if Map[player_zone[0]][player_zone[1]][j][i] == 1:
                pg.draw.rect(mapSurface, MAINGREY, (i*50,j*50,50,50), 0)







    #--- while ---#
    RUNNING = True
    while RUNNING:
        root.fill(MAINGREY)

        time += 1/60

        for event in pg.event.get():
            if event.type == pg.QUIT:
                RUNNING = False
            
            if event.type == pg.MOUSEMOTION:
                if running_course == 1:
                    root.blit(picture_mouseButton, (pg.mouse.get_pos()[0]-20, pg.mouse.get_pos()[1]-30))

            if event.type == pg.MOUSEBUTTONDOWN:
                if running_course == 1:
                    if (event.pos[0] > 100 and event.pos[0] < 250) and (event.pos[1] > 200 and event.pos[1] < 280):
                        running_course = 2

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    if Map[player_zone[0]][player_zone[1]][playery-1][playerx] == 0:
                        playery -= 1
                if event.key == pg.K_s:
                    if playery == 13:
                        if playerx == 8:
                            playery = 14
                    elif Map[player_zone[0]][player_zone[1]][playery+1][playerx] == 0:
                        playery += 1
                if event.key == pg.K_a:
                    if Map[player_zone[0]][player_zone[1]][playery][playerx-1] == 0:
                        playerx -= 1
                if event.key == pg.K_d:
                    if playerx == 17:
                        if playery == 6:
                            playerx = 18
                    elif Map[player_zone[0]][player_zone[1]][playery][playerx+1] == 0:
                        playerx += 1
                


        #---  0  ---#
        if time > 0 and time < 5:
            root.fill(BLACK)
        if time > 5 and time < 6:
            running_course = 1
        #动画


        #---  1  ---#
        if time > 7 and running_course == 1:
            root.blit(textOut("寻找鼠标", WHITE, CH), (100,100))
            root.blit(picture_mainButton, (100,200))

        #---  2  ---#
        if playerx < 0 and playery == 6: # 玩家越过左侧
            player_zone = [player_zone[0]-1, player_zone[1]]
            try:
                Map[player_zone[0]][player_zone[1]]
            except:
                Map[player_zone[0]] = {}
                Map[player_zone[0]][player_zone[1]] = omap.omap(900,700,50,True)
            playerx = 17
            playery = 6

        if playerx > 17 and playery == 6: # 玩家越过右侧
            player_zone = [player_zone[0]+1, player_zone[1]]
            try:
                Map[player_zone[0]][player_zone[1]]
            except:
                Map[player_zone[0]] = {}
                Map[player_zone[0]][player_zone[1]] = omap.omap(900,700,50,True)
            playerx = 0
            playery = 6

        if playerx == 8 and playery < 0:
            player_zone = [player_zone[0], player_zone[1]+1]
            try:
                Map[player_zone[0]][player_zone[1]]
            except:
                Map[player_zone[0]][player_zone[1]] = omap.omap(900,700,50,True)
            playerx = 8
            playery = 13

        if playerx == 8 and playery > 13:
            player_zone = [player_zone[0], player_zone[1]-1]
            try:
                Map[player_zone[0]][player_zone[1]]
            except:
                Map[player_zone[0]][player_zone[1]] = omap.omap(900,700,50,True)
            playerx = 8
            playery = 0

        if running_course == 2:
            root.blit(mapSurface, (0,0))
            pg.draw.rect(root,BLUE,(playerx*50+4,playery*50+4,40,40),0)
            '''
            if not (player_zone[0] in Map):
                Map[player_zone[0]] = {}
                Map[player_zone[0]][player_zone[1]] = omap.omap(900,700,50,True)
            if not (player_zone[1] in Map[player_zone[0]]):
                Map[player_zone[0]] = {}
                Map[player_zone[0]][player_zone[1]] = omap.omap(900,700,50,True)
            '''
            pg.draw.rect(mapSurface, WHITE, (0,0,900,700), 0)
            for i in range(18): #行
                for j in range(14): #列
                    if Map[player_zone[0]][player_zone[1]][j][i] == 1:
                        pg.draw.rect(mapSurface, MAINGREY, (i*50,j*50,50,50), 0)





        pg.display.update()
        pg_timer.tick(60) # 帧速率：60pfs

    pg.quit()
except:
    print("出现错误，请联系开发者。")
    print("FOUNDMOUSEBUTTON - 0.0.1 (0.0.0.0)")
    input()