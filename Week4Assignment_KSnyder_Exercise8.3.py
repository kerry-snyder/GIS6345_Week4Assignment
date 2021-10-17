#!/usr/bin/env python
# coding: utf-8

# # Exercise 8.3

# In[ ]:


#The following is a solution for Exercise 6.3 from Github


# In[ ]:


from __future__ import print_function, division


# In[ ]:


def first(word):
    """Returns the first character of a string."""
    return word[0]


# In[ ]:


def last(word):
    """Returns the last of a string."""
    return word[-1]


# In[ ]:


def middle(word):
    """Returns all but the first and last characters of a string."""
    return word[1:-1]


# In[ ]:


def is_palindrome(word):
    """Returns True if word is a palindrome."""
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))


# In[ ]:


print(is_palindrome('redivider'))


# In[ ]:


#The expression [:] returns no part of the string, while [::-1] returns the string in reverse


# In[ ]:


fruit = 'banana'
fruit [:]

fruit[::-1]


# In[ ]:


#First attempt at one-line version of is_palindrome


# In[ ]:


def is_palindrome(word):
    if word [::-1] == word:
        return True
    if word [::-1] != word:
        return False 


# In[ ]:


print(is_palindrome('redivider'))


# In[ ]:


print(is_palindrome('red'))


# In[ ]:


#Second attempt at one-line version of is_palindrome 


# In[ ]:


def is_palindrome(word): return True if word [::-1] == word else False


# In[ ]:


print(is_palindrome('redivider'))


# In[ ]:


print(is_palindrome('red'))


# In[ ]:




