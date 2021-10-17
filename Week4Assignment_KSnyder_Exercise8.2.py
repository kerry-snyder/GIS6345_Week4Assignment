#!/usr/bin/env python
# coding: utf-8

# # Exercise 8.2

# In[ ]:


#Example of function in Section 8.7


# In[ ]:


word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)


# In[ ]:


#str.count(sub[, start[, end]])


# In[ ]:


#Another way to describe the syntax is string.count(string, start_index,end_index)


# In[ ]:


#Return the number of non-overlapping occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.


# In[ ]:


string = "banana"
print(string.count("a",0,6))

