#!usr/bin/python3

import random
import pandas as pd
import os
import sys

def key_count(x1):   
    def key_in():
        try:
            n = input('count: ')
            if n == 'end':
                sys.exit()
        except ValueError:
            print('請輸入整數！')
            n = input('count: ')
        error = 0
        for i in range(int(n)):
            error += x1()
        if error == 0:
            print('恭喜你！太完美了！')
        else:
            print(f'可惜錯了{error}個！')
    return key_in


@key_count
def word_read():
    error_count = 0        
    w = random.choice(words)
    print(f'EN: {w[0]}\nTW: {w[1]}')
    keyin = input('keyin: ')
    if keyin.lower() == 'end':
        print('close……')
        sys.exit()
    elif keyin.lower() == w[0].lower():
        print('ok')
    else:
        print('error')
        error_count = 1
    return error_count
        

print("請輸入練習次數 or 輸入'end'離開程式")

filepath = os.path.dirname(os.path.abspath(__file__))
allpath = os.path.join(filepath, 'words.csv')
df1 = pd.read_csv(allpath)
df1.columns = ['1', '2', 'en', 'tw' ]
ens = df1['en']
tws = df1['tw']
enandtw = zip(ens, tws)
words = list(enandtw)
print(type(words))
    
#word_read()

