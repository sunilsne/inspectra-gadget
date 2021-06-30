#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


import glob


# In[3]:


import pandas as pd


# In[4]:


import bs4 as bs


# In[5]:


from bs4 import BeautifulSoup


# In[6]:


##Generate empty list of PIDs
PIDs = []


# In[7]:


##Populate list of PIDs
for filename in glob.iglob('/grp/hst/cos2/cosmo/*', recursive=True):
    file_name = filename[20:]
    PIDs.append(file_name)


# In[8]:


##Generate empty list of PIDs that have EtcRunIds
PIDs_with_etcrunid = []


# In[9]:


##Filtering
for value in PIDs:
    if len(value) == 5:
        PIDs_with_etcrunid.append(value)
    else:
        pass


# In[10]:


##Populating list of PIDs with EtcRunIds
Ordered_PIDs_with_etcrunids = sorted(PIDs_with_etcrunid)[236:865]


# In[11]:


##Generate empty list of files
files = []


# In[12]:


##Retrieve URLs
for PID in Ordered_PIDs_with_etcrunids:
    URL = 'https://www.stsci.edu/hst/phase2-public/'+PID+'.apt'
    files.append(URL)


# In[13]:


##Generate empty list to hold page numbers
pagenumbers = []


# In[14]:


for key in range(626):
    pagename = 'page'+str(key)
    pagenumbers.append(pagename)
pagenumbers


# In[15]:


exposure_names = []


# In[16]:


for z in range(626):
    exposure_name = 'exposure' + str(z)
    exposure_names.append(exposure_name)


# In[17]:


for filenumber in range(626):
    page = requests.get(files[filenumber])
    pagenumbers[filenumber] = bs.BeautifulSoup(page.text, 'lxml')
    exposure_names[filenumber] = pagenumbers[filenumber].find_all('exposure')


# In[18]:


exposure_names


# In[60]:


etc_run_ids = []


# In[61]:


rejects = []


# In[62]:


for j in range(626):
    for i in exposure_names[j]:
        attributes_dictionary = i.attrs
        run_id = (attributes_dictionary.get('etcrunid'))
        if 'COS' in str(run_id) or 'Cos' in str(run_id) or 'COs' in str(run_id) or 'cos' in str(run_id):
            etc_run_ids.append(run_id)
        else:
            rejects.append(run_id)


# In[63]:


results = list(set(etc_run_ids))
results


# In[64]:


list(set(rejects))


# In[65]:


textfile = open('/users/ssunilkumar/desktop/cos_data/etcrunid_list.txt', "w")
for element in results:
    textfile.write(element + "\n")
textfile.close()


# In[66]:


textfile_rejects = open('/users/ssunilkumar/desktop/cos_data/reject_list.txt', 'w')
for o in rejects:
    textfile_rejects.write(str(o) + '\n')
textfile.close()


# In[67]:


textfile


# In[68]:


textfile_rejects


# In[ ]:


##single file##


# In[ ]:


file = requests.get(files[607])


# In[ ]:


parsed_file = bs.BeautifulSoup(file.text, 'lxml')


# In[ ]:


##Generate list of exposures
exposures = parsed_file.find_all('exposure')


# In[ ]:


EtcRunIds = []


# In[ ]:


for i in exposures:
    attributes_dictionary = i.attrs
    EtcRunId = (attributes_dictionary.get('etcrunid'))
    EtcRunIds.append(EtcRunId)


# In[ ]:


Unique_EtcRunIds = list(set(EtcRunIds))


# In[ ]:


Unique_EtcRunIds

