import sys
import random
import time
import os
import threading as thr
import asyncio
import sqlfunc

MENU = {'1':10, '2':30, '3':50, '4':100, '5':sys.exit}

class EnKeyIn(sqlfunc.Sql_Create):
    
    def __init__(self):
        super().__init__()
        self.words = self.sql_find()
        self.complete_time = 0
        self.count_total = 0
        self.error_count = 0
        self.w_quan = 0
        self.error_rate = 0
        #self.judge_thread = 0
        self.time_start = 0
        self.time_end = 0

    def menu_select(self):
        ms = input('請選擇單字個數：')
        if ms in '1234':
            self.w_quan = MENU.get(ms)
            self.count_total = MENU.get(ms)
            self.word_quantity(MENU.get(ms))
        else:
            sys.exit()
        
    def word_quantity(self, quan):
        words_temp = random.sample(self.words, k=quan)
        self.time_start = time.time()
        while words_temp:
            try:
                wt = words_temp.pop()
                print()
                print(f"單字：{wt[1]}\n翻譯：{wt[2]}")
                print()
                ei = self.en_input()
                if ei.lower() == wt[1].lower():
                    print('ok')
                else:
                    self.error_count += 1
                    print('error')        
            except AttributeError:
                self.error_count += 1
                print('error')
        self.time_end = time.time()
        self.evaluation()

    def en_input(self):
        w = input('輸入英文：')
        if w.isalpha():
            return w

    def evaluation(self):
        self.complete_time = self.time_end - self.time_start
        self.error_rate = self.error_count / self.w_quan
        print()
        print(f'花費時間：{self.complete_time:06.2f}')
        print(f'錯誤率：{self.error_rate:3.2%}')

    def total_average(self):
        pass
    

def display_ENT():
    act = 'clear' if sys.platform.startswith('linux') else 'cls'
    os.system(act)


def display_view():        
    print('=================')
    print('ENType')
    print('=================')
    print('1. 10個單字')
    print('2. 30個單字')
    print('3. 50個單字')
    print('4. 100個單字')
    print('5. 結束程式')
    print('=================')


display_view()
obj = EnKeyIn()
obj.menu_select()
