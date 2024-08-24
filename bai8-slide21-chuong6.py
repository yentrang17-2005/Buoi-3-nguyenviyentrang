# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 15:19:06 2024

@author: Admin
"""

A = (32)**0.2-(1/64)**(-0.25)+(8/27)**(1/3)
print('ket qua:',round(A,3))

import math
a = int(input('Nhap so thuc a:'))
b = int(input('Nhap so thuc b:'))
B = (math.sqrt(a)-math.sqrt(b))/(a**(1/4)-b**(1/4))-(math.sqrt(a)+(a*b)**(1/4))/(a**(1/4)+b**(1/4))
print('ket quả là:',B)
