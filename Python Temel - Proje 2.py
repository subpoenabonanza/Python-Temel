#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def anti(input):
    output = []
    for i in input[::-1]:
        for j in range(1):
            output.append(i[::-1])
    return output

