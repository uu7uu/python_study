#!/usr/bin/env python
# coding: utf-8

# In[1]:


#创建Die类 py文件
from random import randint
class Die():
    """表示一个骰子的类"""
    def __init__(self,num_sides=6):
        self.num_sides = num_sides
    def roll(self):
        return randint(1,self.num_sides)


# In[ ]:




