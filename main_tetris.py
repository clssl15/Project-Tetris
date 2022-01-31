# -*- coding: utf-8 -*-
import time
import os
import random
import copy
from pynput import keyboard
from pynput.keyboard import Key, Controller

end=0

background=[['_','_','_','_','_','_','_','_','_','_','_','_'],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
            ['-','-','-','-','-','-','-','-','-','-','-','-']
           ]
block=[[[0,0,1,1,1,1,0,0,0],[0,1,0,0,1,0,0,1,1],[0,0,0,1,1,1,1,0,0],[1,1,0,0,1,0,0,1,0]],
       [[1,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,1,0],[0,0,0,1,1,1,0,0,1],[0,1,0,0,1,0,1,1,0]],
       [[0,1,1,1,1,0,0,0,0],[0,1,0,0,1,1,0,0,1],[0,0,0,0,1,1,1,1,0],[1,0,0,1,1,0,0,1,0]],
       [[1,1,0,0,1,1,0,0,0],[0,0,1,0,1,1,0,1,0],[0,0,0,1,1,0,0,1,1],[0,1,0,1,1,0,1,0,0]],
       [[0,1,0,1,1,1,0,0,0],[0,1,0,0,1,1,0,1,0],[0,0,0,1,1,1,0,1,0],[0,1,0,1,1,0,0,1,0]],
       [[1,1,0,1,1,0,0,0,0],[0,1,1,0,1,1,0,0,0],[0,0,0,0,1,1,0,1,1],[0,0,0,1,1,0,1,1,0]],
       [[0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0],[0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0],[0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0]]
       ]
    
def bgprint(row,col,v): #row=point[0], col=point[1], v=회전체 중 선택된 블록
    global imsi_bg
    imsi_bg=copy.deepcopy(background)
    k=0
    for i in range(0,3+int(n/6)):
        for j in range(0,3+int(n/6)):
            if block[n][v][k]:
                imsi_bg[row+i][col+j]="*"
            k+=1

    os.system('cls')
    for i in range(len(imsi_bg)):
        print(''.join(imsi_bg[i]))

def is_block(row,col,v):
    k=0
    for i in range(0,3+int(n/6)):
        for j in range(0,3+int(n/6)):
            if block[n][v][k]==1 and background[row+i][col+j]!=' ':
                return 0
            k+=1
    return 1

def modify_bg(row,col,v):
    global sw
    sw=1
    k=0
    for i in range(0,3+int(n/6)):
        for j in range(0,3+int(n/6)):
            if block[n][v][k]:
                background[row+i][col+j]='*'
            k+=1
            
def on_press(key):
    if key== keyboard.Key.down:
        num=is_block(point[0]+1,point[1],rotate)
        if num==0: modify_bg(point[0],point[1],rotate)
        point[0]+=num
    elif key== keyboard.Key.left:
        num=is_block(point[0],point[1]-1,rotate)
        point[1]-=num
    elif key== keyboard.Key.right:
        num=is_block(point[0]+1,point[1]+1,rotate)
        point[1]+=num
    bgprint(point[0],point[1],rotate)

def falling_block():
    num=is_block(point[0]+1,point[1],rotate)
    if num==0: modify_bg(point[0],point[1],rotate)
    point[0]+=num
    bgprint(point[0],point[1],rotate)

if __name__ == '__main__':
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    imsi_bg=copy.deepcopy(background) #imsi_bg는 background의 값을 할당받지만, 같은 주소값을 가지는 것은 아님.
    while(end==0):
        point=[2,4]
        rotate=0
        sw=0
        n=random.randint(0,6)
        bgprint(point[0],point[1],rotate)
        while(sw==0):
            time.sleep(1.5)
            falling_block()