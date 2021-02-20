# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 20:06:46 2021

@author: SedriKor
"""

def bubble(list):
    for i in range(1,len(list)):
        for j in range(len(list)):
            if list[j] > list[i]:
                list[j], list[i] = list[i], list[j]
            else:
                continue
            print(list)
        print('round: ' + str(i) + str(list)) 
        if list[0] < list[1] < list[2] < list[3] < list[4]:
            break
    return

import random

if __name__ =='__main__':
    list = []
    for s in range(5):
        a = int(random.randint(1, 100))
        list.append(a)
        
    # list = [2,31,42,21,6,23]
    print('origin :' + str(list))
    bubble(list)