#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items

def convert_int_to_bin(dec_num):
    s=Stack()
    bin_num=""
    rem=None
    while dec_num!=0:
        rem=dec_num%2
        s.push(rem)
        dec_num=dec_num//2
    while not s.is_empty():
        bin_num += str(s.pop())
    return bin_num


# In[4]:


int(convert_int_to_bin(56),2)


# In[5]:


print(int(convert_int_to_bin(56),2)==56)


# In[ ]:




