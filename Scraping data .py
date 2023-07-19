#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup 
import requests 


# In[2]:


url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_India"
page = requests.get(url)

soup = BeautifulSoup(page.text , 'html')


# In[163]:


print(soup)


# In[164]:


soup.find('table' , class_ = 'wikitable sortable')


# In[13]:


table = soup.find('table')


# In[21]:


world_title = table.find_all('th')
world_title 


# In[22]:


world_table_title = [title.text.strip() for title in world_title]
world_table_title


# In[100]:


import pandas as pd 


# In[103]:


df = pd.DataFrame(columns = world_table_title  )
df


# In[104]:


column_data = table.find_all('tr')


# In[105]:


#pulling out rows 


for rows in column_data[1:]:
    row_data = rows.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data] 
    print(individual_row_data)
    
    


# In[130]:


#loop each iteration and put the value in our dataframe 

for rows in column_data[1:]:
    row_data = rows.find_all('td')
    
    
    
    individual_row_data = [data.text.strip() for data in row_data]
    
    
    merged_list = []
    for i in range(0, 4, 2):
        merged_value = individual_row_data[i] + individual_row_data[i + 1]
        merged_list.append(merged_value)
    merged_list.extend(individual_row_data[4:])
    print(merged_list)
    
    length_df = len(df)
    df.loc[length_df] = merged_value
    
    
    


# In[131]:


df


# In[162]:


df.to_csv(r"/Users/nidhirathod/Desktop/web\ scraping list of largest companies in india.csv",index = False)




# 

# In[ ]:




