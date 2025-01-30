# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 17:11:55 2025

@author: Liv, Kyle
"""

def boat(dictn, n=100):
    dictn = dict(sorted(dictn.items(), key=lambda x:x[1], reverse=True))
    for left in dictn.copy():
        if len(dictn) == 1:
            if dictn[left] > 100:
                print(left, "can't cross")
            else:
                print([left])
            break
        for right in dictn.copy():
            pass
        if dictn[left] > n:
            print(left, "can not cross.")
            del dictn[left]
            continue
        if dictn[right] > n:
            print(right, "can not cross.")
            del dictn[right]
            continue
        else:
            partner = dictn[left] + dictn[right]
            if partner > 100:
                print([left])
                del dictn[left]
            else:
                print([left, right])
                del dictn[left]
                del dictn[right]
        if dictn == {}:
            break

#Question:
peep = {'Roman':90, 'Verlyn':80, 'Lloyd':60, 'Robin':40, 'Supplies':20}

#ANSWER:
boat(peep)