#!/usr/bin/env python
# coding: utf-8

# In[137]:


import requests


# In[138]:


import xml.etree.ElementTree as ET


# In[139]:





# In[140]:


from bs4 import BeautifulSoup


# In[141]:


file = requests.get("https://www.stsci.edu/hst/phase2-public/16430.apt")
file.content


# In[133]:


soup = BeautifulSoup(file.content, 'html.parser')


# In[134]:


list(soup.children)


# In[135]:


exposures = soup.find_all('exposuretime')
list(exposures)


# In[136]:


ETCRunId = exposures[8].get_text()
print(ETCRunId)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




