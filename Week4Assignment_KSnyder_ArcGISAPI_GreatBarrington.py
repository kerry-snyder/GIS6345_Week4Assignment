#The following is code created through an ArcGIS Online notebook. I mapped Great Barrington, Massachusetts, where I was born.
#!/usr/bin/env python
# coding: utf-8

# ## Welcome to your notebook.
# 

# #### Run this cell to connect to your GIS and get started:

# In[ ]:


from arcgis.gis import GIS
gis = GIS("home")


# #### Now you are ready to start!

# In[ ]:


map1 = gis.map('Great Barrington, MA')


# In[ ]:


map1


# In[ ]:


# Item Added From Toolbar
# Title: USA Parks | Type: Feature Service | Owner: esri_dm
item = gis.content.get("f092c20803a047cba81fbf1e30eff0b5")
item


# In[ ]:


map1.add_layer(item)


# In[ ]:


map1


# In[ ]:


# Item Added From Toolbar
# Title: World Distance to Water | Type: Image Service | Owner: esri
item2 = gis.content.get("46cbfa5ac94743e4933b6896f1dcecfd")
item2


# In[ ]:


map1.add_layer(item2)


# In[ ]:


map1


# In[ ]:


# Item Added From Toolbar
# Title: Global Roads Open Access Data Set, Version 1 (gROADSv1) | Type: Map Service | Owner: Columbia
item3 = gis.content.get("de90ef9d861e480b9ebccc7cefb29de9")
item3


# In[ ]:


map1.add_layer(item3)


# In[ ]:


map1


# In[ ]:




