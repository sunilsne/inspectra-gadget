#!/usr/bin/env python
# coding: utf-8

# In[1]:

import requests

# In[2]:

import glob

# In[3]:

import bs4 as bs

# In[4]:

from bs4 import BeautifulSoup

# In[5]:

##Generate empty list of PIDs
PIDs = []

# In[6]:

##Populate list of PIDs
for filename in glob.iglob('/grp/hst/cos2/cosmo/*', recursive=True):
    file_name = filename[20:]
    PIDs.append(file_name)

# In[7]:

##Generate empty list of PIDs that have EtcRunIds
PIDs_with_etcrunid = []

# In[8]:

##Filtering
for value in PIDs:
    if len(value) == 5:
        PIDs_with_etcrunid.append(value)
    else:
        pass

# In[9]:

##Populating list of PIDs with EtcRunIds
Ordered_PIDs_with_etcrunids = sorted(PIDs_with_etcrunid)[236:865]

# In[10]:

##Generate empty list of files
files = []

# In[11]:

##Retrieve URLs
for PID in Ordered_PIDs_with_etcrunids:
    URL = 'https://www.stsci.edu/hst/phase2-public/'+PID+'.apt'
    files.append(URL)

# In[12]:

##Generate empty list to hold page numbers
pagenumbers = []

# In[13]:

##Assign page numbers to keep track of files
for key in range(626):
    pagename = 'page'+str(key)
    pagenumbers.append(pagename)

# In[14]:

##Generate empty list of beautiful soup objects
exposure_names = []

# In[15]:

##Populate list of exposures
for z in range(626):
    exposure_name = 'exposure' + str(z)
    exposure_names.append(exposure_name)

# In[16]:

##Parse xml files
for filenumber in range(626):
    page = requests.get(files[filenumber])
    pagenumbers[filenumber] = bs.BeautifulSoup(page.text, 'lxml')
    exposure_names[filenumber] = pagenumbers[filenumber].find_all('exposure')

# In[17]:

##Generate empty list of run ids
etc_run_ids = []

# In[18]:

##Generate empty list of stis/other unwanted data
rejects = []

# In[19]:

##Search for run ids in each file
for j in range(626):
    for i in exposure_names[j]:
        attributes_dictionary = i.attrs
        run_id = (attributes_dictionary.get('etcrunid'))
        if 'COS' in str(run_id) or 'Cos' in str(run_id) or 'COs' in str(run_id) or 'cos' in str(run_id):
            etc_run_ids.append(run_id)
        else:
            rejects.append(run_id)

# In[20]:

##Populate results list
results = list(set(etc_run_ids))

# In[21]:

##Populate reject list
list(set(rejects))

# In[22]:

##Write results to results file
textfile = open('/users/ssunilkumar/desktop/cos_data/etcrunid_list.txt', "w")
for element in results:
    textfile.write(element + "\n")
textfile.close()

# In[23]:

##Write rejects to file
textfile_rejects = open('/users/ssunilkumar/desktop/cos_data/reject_list.txt', 'w')
for o in rejects:
    textfile_rejects.write(str(o) + '\n')
textfile.close()

# In[24]:

textfile

# In[25]:

textfile_rejects

##single file##

# In[26]:

file = requests.get(files[607])

# In[27]:

parsed_file = bs.BeautifulSoup(file.text, 'lxml')

# In[28]:

##Generate list of exposures
exposures = parsed_file.find_all('exposure')

# In[29]:

EtcRunIds = []

# In[30]:

for i in exposures:
    attributes_dictionary = i.attrs
    EtcRunId = (attributes_dictionary.get('etcrunid'))
    EtcRunIds.append(EtcRunId)

# In[31]:

Unique_EtcRunIds = list(set(EtcRunIds))

# In[32]:

Unique_EtcRunIds
