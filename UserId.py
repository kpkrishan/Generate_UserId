#!/usr/bin/env python
# coding: utf-8

# In[57]:


def userId(first,last,pin,n):
    if len(first)>len(last):
        smaller=last
        longer=first
    elif len(first)<len(last):
        smaller=first
        longer=last
    else:
        for i in range(len(first)):
            if first[i]<last[i]:
                smaller=first
                longer=last
            else:
                smaller=last
                longer=first
    
    lst=[x for x in str(pin)]
    m=''
    for i in range(len(lst)):
        if i==n:
            m=m+lst[i-1] 

    l=''
    rev=list(reversed(lst))
    for j in range(len(rev)):
        if j==n:
            l=l+rev[j-1]
    
    userId=longer[0]+smaller+str(m)+str(l)
    print(userId.swapcase())  

first=input()
last=input()
pin=int(input())
n=int(input())

userId(first,last,pin,n)


# In[ ]:




