#!usr/bin/python3

import random
import pandas as pd
import os
import sys

def key_count(x1):   
    def key_in():
        n = int(input('count: '))
        for i in range(n):
            x1()
    return key_in

        
@key_count
def word_read():    
    w = random.choice(words)
    print(w)
    keyin = input('word: ')
    if keyin == 'end':
        print('close……')
        sys.exit()
    elif keyin == w[0]:
        print('ok')
    else:
        print('error')
    
filepath = os.path.dirname(os.path.abspath(__file__))
allpath = os.path.join(filepath, 'words.csv')
df1 = pd.read_csv(allpath)
df1.columns = ['1', '2', 'en', 'tw' ]
a = df1.loc[:, 'en']
b = df1.loc[:,'tw']
c = zip(a, b)
words = list(c)
    
word_read()

