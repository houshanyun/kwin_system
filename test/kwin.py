#!usr/bin/python3

import random
import pandas as pd
import os
import sys

### 功能函數 ###

class KeyinEx:
    def __init__(self, words, exCount=0, erCount=0):
        self.words = words
        self.exCount = exCount
        self.erCount = erCount
    

    def mycount(self):
        while True:
            try:
                Count = input('count: ')
                if Count == 'end':
                    print('close……')
                    testk.close_sys()
                else:
                    self.exCount = int(Count)
                    break
            except Exception as e:
                print('錯誤訊息：', e)
                print('請輸入整數！')
                continue
        

    def word_put(self):
        temp_space = list()
        temp_space = random.sample(self.words, k=self.exCount)
        while temp_space:
            w = temp_space.pop()
            print(f'EN:{w[0]}\nTW:{w[1]}')
            key_in = input('keyin: ')
            if key_in.lower() == w[0].lower():
                print('ok')
            else:
                print('error')
                self.erCount += 1
    

    def close_sys(self):
        sys.exit()


    def level(self):
        if self.erCount == 0:
            print('恭喜你！太完美了！')
        else:
            print(f'可惜錯了{self.erCount}個！')


class DataCsv:
    def __init__(self, allpath):
        self.path = allpath
        self.df = pd.read_csv(self.path)   
        

    def outcsv(self):
        self.df.columns = ['1', '2', 'en', 'tw' ]
        ens = self.df['en']
        tws = self.df['tw']
        enandtw = zip(ens, tws)
        words = list(enandtw)
        return words


### 資料處理 ###
print("請輸入練習次數 or 輸入'end'離開程式")
filepath = os.path.dirname(os.path.abspath(__file__))
allpath = os.path.join(filepath, 'words.csv')


### 主程式 ###
csvdata = DataCsv(allpath)
words = csvdata.outcsv()

testk = KeyinEx(words)
testk.mycount()
testk.word_put()
testk.level()
