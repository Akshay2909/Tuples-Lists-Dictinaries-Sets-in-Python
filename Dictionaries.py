#!/usr/bin/env python
# coding: utf-8

# <h2 id="Dic">Dictionaries</h2>
# 

# <h3 id="content">What are Dictionaries?</h3>
# 

# A dictionary consists of keys and values. It is helpful to compare a dictionary to a list. Instead of being indexed numerically like a list, dictionaries have keys. These keys are the keys that are used to access values within a dictionary.
# 

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/DictsList.png" width="650" />
# 

# An example of a Dictionary <code>Dict</code>:
# 

# In[1]:


# Create the dictionary

Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
Dict


# The keys can be strings:
# 

# In[2]:


# Access to the value by the key

Dict["key1"]


# Keys can also be any immutable object such as a tuple:
# 

# In[3]:


# Access to the value by the key

Dict[(0, 1)]


# Each key is separated from its value by a colon "<code>:</code>".  Commas separate the items, and the whole dictionary is enclosed in curly braces. An empty dictionary without any items is written with just two curly braces, like this  "<code>{}</code>".
# 

# In[4]:


# Create a sample dictionary

release_year_dict = {"Thriller": "1982", "Back in Black": "1980",                     "The Dark Side of the Moon": "1973", "The Bodyguard": "1992",                     "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976",                     "Saturday Night Fever": "1977", "Rumours": "1977"}
release_year_dict


# In summary, like a list, a dictionary holds a sequence of elements. Each element is represented by a key and its corresponding value. Dictionaries are created with two curly braces containing keys and values separated by a colon. For every key, there can only be one single value, however,  multiple keys can hold the same value. Keys can only be strings, numbers, or tuples, but values can be any data type.
# 

# It is helpful to visualize the dictionary as a table, as in the following image. The first column represents the keys, the second column represents the values.
# 

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/DictsStructure.png" width="650" />
# 

# <h3 id="key">Keys</h3>
# 

# You can retrieve the values based on the names:
# 

# In[5]:


# Get value by keys

release_year_dict['Thriller'] 


# This corresponds to:
# 

# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/DictsKeyOne.png" width="500" />
# 

# Similarly for <b>The Bodyguard</b>
# 

# In[6]:


# Get value by key

release_year_dict['The Bodyguard'] 


# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/DictsKeyTwo.png" width="500" />
# 

# Now let us retrieve the keys of the dictionary using the method <code>keys()</code>:
# 

# In[7]:


# Get all the keys in dictionary

release_year_dict.keys() 


# You can retrieve the values using the method  <code>values()</code>:
# 

# In[8]:


# Get all the values in dictionary

release_year_dict.values() 


# We can add an entry:
# 

# In[9]:


# Append value with key into dictionary

release_year_dict['Graduation'] = '2007'
release_year_dict


# We can delete an entry:
# 

# In[10]:


# Delete entries by key

del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
release_year_dict


# We can verify if an element is in the dictionary:
# 

# In[11]:


# Verify the key is in the dictionary

'The Bodyguard' in release_year_dict


# <hr>
# 

# <h2 id="quiz">Quiz on Dictionaries</h2>
# 

# <b>You will need this dictionary for the next two questions:</b>
# 

# In[12]:


# Question sample dictionary

soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
soundtrack_dic 


# a) In the dictionary <code>soundtrack_dic</code> what are the keys ?
# 

# In[13]:


# Write your code below and press Shift+Enter to execute
soundtrack_dic.keys()


# b) In the dictionary <code>soundtrack_dic</code> what are the values ?
# 

# In[14]:


# Write your code below and press Shift+Enter to execute
soundtrack_dic.values()


# <hr>
# 

# <b>You will need this dictionary for the following questions:</b>
# 

# The Albums <b>Back in Black</b>, <b>The Bodyguard</b> and <b>Thriller</b> have the following music recording sales in millions 50, 50 and 65 respectively:
# 

# a) Create a dictionary <code>album_sales_dict</code> where the keys are the album name and the sales in millions are the values.
# 

# In[22]:


# Write your code below and press Shift+Enter to execute
album_sales_dict = {"Back in Black":50,"The Bodyguard":50," Thriller":65}
album_sales_dict


# b) Use the dictionary to find the total sales of <b>Thriller</b>:
# 

# In[25]:


# Write your code below and press Shift+Enter to execute
album_sales_dict[' Thriller']


# c) Find the names of the albums from the dictionary using the method <code>keys()</code>:
# 

# In[2]:


# Write your code below and press Shift+Enter to execute
album_sales_dict = {"Back in Black":50,"The Bodyguard":50," Thriller":65}
album_sales_dict.keys()


# d) Find the values of the recording sales from the dictionary using the method <code>values</code>:
# 

# In[3]:


# Write your code below and press Shift+Enter to execute
album_sales_dict = {"Back in Black":50,"The Bodyguard":50," Thriller":65}
album_sales_dict.values()

