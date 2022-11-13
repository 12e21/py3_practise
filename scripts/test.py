#!/usr/bin/python3
#上面这句用于指定解释器路径
from sys import argv
#number_1=int(argv[1])
#number_2=int(argv[2])
#print('加数1:',number_1,'加数2:',number_2,'和：',number_1+number_2)
IP={'000.000.000.000',254}
if 255 in IP:
    print('255在集合中')
else:
    print('255不在集合中')
