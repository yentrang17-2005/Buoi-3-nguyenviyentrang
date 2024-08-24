# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 17:03:10 2024

@author: Admin
"""

a="Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
print(a.split(","))
b=a.replace("P.","").replace("Q.","").replace("Tp.","")
print(b)