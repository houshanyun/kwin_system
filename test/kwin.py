import random
import pandas as pd
import os
import sys
import threading as thr
import time

from sqlfunc import Sql_Create 

### 功能函數 ###

class EnType:
    def __init__(self, words, exCount=0, erCount=0):
        self.words = words
        self.exCount = exCount
        self.erCount = erCount
    

    def mycount(self):
        while True:
            try:
                Count = input('練習的單字數量: ' )
                if Count == 'end':
                    print('close……')
                    sys.exit()
                elif Count.isnumeric():
                    if 1 <= int(Count) <= 50:
                        self.exCount = int(Count)
                        break
                    else:
                        print('請輸入1~50之間的數字')
                else:
                    print('請輸入整數！')
            except Exception as e:
                print('錯誤訊息：', e)
                print('請輸入整數！')
        
    
    
    def word_out(self):
        temp_space = list()
        temp_space = random.sample(self.words, k=self.exCount)
        while temp_space:
            w = temp_space.pop()
            print(f'EN:{w[1]}\tTW:{w[2]}')
            inword = yield
            if inword.lower() == w[1].lower():
                print('ok')
            else:
                print('error')
                self.erCount += 1
                if w[3] is None:
                    sq.sql_edit(1, w[0])
                else:
                    sq.sql_edit(list(w)[3]+1, w[0])
                    
        
    def level(self):
        if not self.erCount:
            print('恭喜你！太完美了！')
        else:
            print(f'可惜錯了{self.erCount}個！')
    

    def word_put(self):
        a = self.word_out()
        a.send(None)
        while True:
            try:
                key_in = input('keyin: ')
                a.send(key_in)
            except:
                break
        

def timing(t):
    for i in range(1, 51):
        s = '=' * i + '*' * (50 - i) 
        sys.stdout.write(f'\r[{s}]')
        sys.stdout.flush()
        time.sleep(t)
    else:
        print()


### 主程式 ###

print("請輸入練習次數（1~50之間的數字） or 輸入'end'離開程式")

sq = Sql_Create()
word_data = sq.sql_find()

obj = EnType(word_data)
obj.mycount()
obj.word_out()
obj.word_put()
obj.level()

sq.sql_send()
sq.sql_end()
