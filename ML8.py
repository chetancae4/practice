#!/usr/bin/env python
# coding: utf-8

# In[1]:


#let us consider i wrote a function and if my fraind needs that function  i can share the code by making its module
#fr making module there will be no functional calls and jupyter extension is not .py it is ipymb so we have to change
#goto file->download as->python(py)
#functions 
#1 no argument no return type
def function1():
    print("hello knowledge shelf")


# In[2]:


def add():
    var1=int(input("enter the value of num1"))
    var2=int(input("enter the value of num2"))
    var3=var1+var2
    print("sum",var3)
    


# In[3]:


#with arg and no return type
def sub(var1,var2):
    var3=var1-var2
    print("sub= ",var3)


# In[4]:


#no arg with return type
def multiply():
    var1=int(input("enter the value of num1"))
    var2=int(input("enter the value of num2"))
    var3=var1*var2
    return var3


# In[5]:


#with arg and with return type
def div(var1,var2):
    var3=var1/var2
    return var3

    


# In[ ]:




