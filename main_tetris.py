# -*- coding: utf-8 -*-
import time
import os
import random
import copy
from pynput import keyboard
from pynput.keyboard import Key, Controller


point=[2,5]
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
    for i in range(-1,2):
        for j in range(-1,2):
            if block[n][v][k]:
                imsi_bg[row+i][col+j]="*"
            k+=1

    os.system('cls')
    for i in range(len(imsi_bg)):
        print(''.join(imsi_bg[i]))

def on_press(key):
    if key== keyboard.Key.up:
        point[0]-=1
    elif key== keyboard.Key.down:
        point[0]+=1
    elif key== keyboard.Key.left:
        point[1]-=1
    elif key== keyboard.Key.right:
        point[1]+=1
    bgprint(point[0],point[1],rotate)
    
if __name__ == '__main__':
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    imsi_bg=copy.deepcopy(background) #imsi_bg는 background의 값을 할당받지만, 같은 주소값을 가지는 것은 아님.
    while(end==0):
        rotate=0
        n=random.randint(0,6)
        bgprint(point[0],point[1],rotate)
        time.sleep(100)