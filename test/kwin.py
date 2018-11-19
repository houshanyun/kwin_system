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
                Count = input('練習次數: ')
                if Count == 'end':
                    print('close……')
                    sys.exit()
                elif Count.isdigit():
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
    
    
    def word_put(self):
        temp_space = list()
        temp_space = random.sample(self.words, k=self.exCount)
        while temp_space:
            w = temp_space.pop()
            print(f'EN:{w[0]}\tTW:{w[1]}')
            key_in = input('keyin: ')
            if key_in.lower() == w[0].lower():
                print('ok')
            else:
                print('error')
                self.erCount += 1
    
        
    def level(self):
        if self.erCount == 0:
            print('恭喜你！太完美了！')
        else:
            print(f'可惜錯了{self.erCount}個！')

### 資料處理 ###

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


filepath = os.path.dirname(os.path.abspath(__file__))
wpath = os.path.join(filepath, 'words.csv')

### 主程式 ###

print("請輸入練習次數（1~50之間的數字） or 輸入'end'離開程式")

csvdata = DataCsv(wpath)
words = csvdata.outcsv()

testk = KeyinEx(words)
testk.mycount()
testk.word_put()
testk.level()
