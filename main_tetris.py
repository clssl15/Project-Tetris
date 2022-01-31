# -*- coding: utf-8 -*-
import time
import os
import random
import copy
from pynput import keyboard
from pynput.keyboard import Key, Controller

end=0

background=[['_','_','_','_','_','_','_','_','_','_','_','_',' '],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' '],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' '],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' '],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' '],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' '],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' '],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' '],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' '],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' '],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' '],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' '],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' '],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' '],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' '],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' '],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' '],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' '],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' '],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' '],
            ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|',' '],
            ['-','-','-','-','-','-','-','-','-','-','-','-',' ']
           ]
block=[[[0,0,1,1,1,1,0,0,0],[0,1,0,0,1,0,0,1,1],[0,0,0,1,1,1,1,0,0],[1,1,0,0,1,0,0,1,0]],
       [[1,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,1,0],[0,0,0,1,1,1,0,0,1],[0,1,0,0,1,0,1,1,0]],
       [[0,1,1,1,1,0,0,0,0],[0,1,0,0,1,1,0,0,1],[0,1,1,1,1,0,0,0,0],[0,1,0,0,1,1,0,0,1]],
       [[1,1,0,0,1,1,0,0,0],[0,0,1,0,1,1,0,1,0],[1,1,0,0,1,1,0,0,0],[0,0,1,0,1,1,0,1,0]],
       [[0,1,0,1,1,1,0,0,0],[0,1,0,0,1,1,0,1,0],[0,0,0,1,1,1,0,1,0],[0,1,0,1,1,0,0,1,0]],
       [[1,1,0,1,1,0,0,0,0],[1,1,0,1,1,0,0,0,0],[1,1,0,1,1,0,0,0,0],[1,1,0,1,1,0,0,0,0]],
       [[0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0],[0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0],]
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

def rotate_block(row,col,v):
    global point, rotate
    k=0
    for i in range(0,3+int(n/6)):
        for j in range(0,3+int(n/6)):
            if block[n][v][k]==1 and background[row+i][col+j]!=' ':
                if i==int(n/6)+2:
                    num=is_block(row-1,col,v)
                    point[0]-=num
                elif j<=1:#왼쪽에서 닿으면 오른쪽으로, 오른쪽에서 닿으면 왼쪽으로.
                    num=is_block(row,col+1,v)
                    point[1]+=num
                else:
                    num=is_block(row,col-1,v)
                    point[1]-=num
                rotate=(rotate+num)%4
                return
            k+=1
    rotate=(rotate+1)%4
    return

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
    global rotate
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
    elif key == keyboard.Key.space:
        rotate_block(point[0],point[1],(rotate+1)%4)
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
        sarray=[]
        n=random.randint(0,6)
        bgprint(point[0],point[1],rotate)
        while(sw==0):
            time.sleep(1.5)
            falling_block()
        for i in range(1,21):
            if background[i][1:11]==['*','*','*','*','*','*','*','*','*','*']:
                background[i][1:11]=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
                sarray.append(i)
        if sarray!=[]:
            os.system('cls')
            for i in range(len(background)):
                print(''.join(background[i]))
            time.sleep(0.5)
        for i in sarray:
            for j in range(i,1,-1):
                background[j][1:11]=background[j-1][1:11]
            background[1][1:11]=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        os.system('cls')
        for i in range(len(background)):
            print(''.join(background[i]))