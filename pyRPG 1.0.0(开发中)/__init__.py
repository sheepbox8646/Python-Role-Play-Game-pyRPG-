"""
版本:1.0.0
主要开发者:箱子,九亿
最近修改时间:2021-04-24
版权所有:Programming Teenager Club, PTC, 编程少年团
"""

import pygame 
import tkinter
import os,sys 
import time
from PIL import Image

print("版权归 '编程少年团' 所有")


'<global>'


#窗口参数
global All_win_length ;All_win_length = 0 #窗口长为几个方砖
global All_win_winth ;All_win_winth = 0 #窗口宽有几个方砖
global All_win_pixlatt ;All_win_pixlatt = 0 #每个方砖的边长为几个像素
global All_win_name ;All_win_name = 0 #窗口标题


'</global>'


class pyRPG:



    class Window:


        def InitMap(le,wi,Pixlatt,name = "news game"):
            """
            (le,wi):设置长有le个方砖,宽有wi个方砖
            Pixlatt:设置每个方砖的边长为Pixlatt个像素
            name:窗口标题
            """

            #将窗口数据赋值给全局变量
            global All_win_length ;All_win_length = int(le)
            global All_win_winth ;All_win_winth = int(wi)
            global All_win_pixlatt ;All_win_pixlatt = int(Pixlatt)

            #初始化窗口
            pygame.init()
            screen=pygame.display.set_mode((int(le) * int(Pixlatt),int(wi) * int(Pixlatt)))
            pygame.display.set_caption(name)


        
    class Tool:
        pass 



    class Floor:
        pass



    class Character:
        pass



    class GameUI:
        pass



    class Action:


        def TileImage(href):

            #如果此图片不是正方形,那么报错
            img = Image.open(href)
            if img.width != img.height:
                raise Exception

            #载入地块图像
            fooimg = pygame.image.load(href)


        def Tile(penetrate = True,DISPLAY = True,ccor = [x,y]):
            """
            penetrate:是否可穿透
            DISPLAY:是否显示
            """
            pygame.screen.blit(fooimg, (int(ccor[0]) * All_win_pixlatt - int(All_win_pixlatt / 2), (int(ccor[1]) * All_win_pixlatt - int(All_win_pixlatt / 2)))
