#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[10]:


from bs4 import BeautifulSoup as soup
import requests
import pandas as pd


# In[ ]:


#1) Write a python program to display all the header tags from wikipedia.org.


# In[30]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://en.wikipedia.org/wiki/Main_Page')
bs = BeautifulSoup(html, "html.parser")
titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
print('List all the header tags :', *titles, sep='\n\n')


# 

# In[ ]:


#2) Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release)
#and make dataframe


# In[14]:


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
 
 
page2=requests.get("https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc")  #Contains top 50 movies
page2a=requests.get("https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&start=51&ref_=adv_nxt")    #Contains corresponding top 50 movies

page2          #As the response is 200, we can proceed with this url
page2a         #As the response is 200, we can proceed with this url

soup2= BeautifulSoup(page2.content)
soup2a= BeautifulSoup(page2a.content)

name=[]            #Empty list to store movie names
for i in soup2.find_all('h3',class_="lister-item-header"):
    l=len(i.text.split())
    name.append(' '.join(i.text.split()[1:l-1]))          #To store only the movie name as a string
for i in soup2a.find_all('h3',class_="lister-item-header"):
    l=len(i.text.split())
    name.append(' '.join(i.text.split()[1:l-1]))

rating=[]         #Empty list to store rating
for i in soup2.find_all('div',class_="inline-block ratings-imdb-rating"):
    rating.append(' '.join(i.text.split()))               #To store only the rating as a string
for i in soup2a.find_all('div',class_="inline-block ratings-imdb-rating"):
    rating.append(' '.join(i.text.split()))

year=[]           #Empty list to store year of release
for i in soup2.find_all('span',class_="lister-item-year text-muted unbold"):
    year.append(i.text.replace('(','').replace(')',''))    #To store only the year of release as a string
for i in soup2a.find_all('span',class_="lister-item-year text-muted unbold"):
    year.append(i.text.replace('(','').replace(')',''))
    
s_no=[]
for j in range(1,101):
    s_no.append(j)

pd.set_option("display.max_rows", None, "display.max_columns", None)                #To display the entire dataframe
df=pd.DataFrame({'Name':name, 'Rating':rating, 'Year of Release': year}, index=s_no)
print("IMDB’s Top rated 100 movies' data")
df


# In[13]:



#3) Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of release) and storing  in dataframe


#https://www.imdb.com/india/top-rated-indian-movies/

page=requests.get("https://www.imdb.com/india/top-rated-indian-movies/?sort=ir,desc&mode=simple&page=1")  

page                 #As the response is 200, we can proceed with this url
             
soup= BeautifulSoup(page3.content)

a=1             #counters to keep top 100 indian movies
b=1
c=1

name=[]            #Empty list to store movie names
for i in soup.find_all('td',class_="titleColumn"):
    l=len(i.text.split())
    if a<=100:                                                #To store top 100 movies
        name.append(' '.join(i.text.split()[1:l-1]))          #To store only the movie name as a string
        a=a+1

rating=[]         #Empty list to store rating
for i in soup.find_all('td',class_="ratingColumn imdbRating"):
    if b<=100:
        rating.append(' '.join(i.text.split()))               #To store only the rating as a string
        b=b+1

year=[]           #Empty list to store year of release
for i in soup.find_all('span',class_="secondaryInfo"):
    if c<=100:
        year.append(i.text.replace('(','').replace(')',''))    #To store only the year of release as a string
        c=c+1
        
s_no=[]
for j in range(1,101):
    s_no.append(j)

pd.set_option("display.max_rows", None, "display.max_columns", None)                #To display the entire dataframe
df=pd.DataFrame({'Name':name, 'Rating':rating, 'Year of Release': year}, index=s_no)
print("IMDB’s Top rated 100 movies' data")
df


# In[ ]:





# In[9]:


#4) Write s python program to display list of respected former presidents of India(i.e. Name , Term of office) 

#https://presidentofindia.nic.in/former-presidents.html

page=requests.get("https://presidentofindia.nic.in/former-presidents.htm")
page           #As the response is 200, we can proceed with this url

soup= BeautifulSoup(page4.content)

pres=[]                   #Empty list to store names of respected former presidents of India
for i in soup.find_all('div',class_="presidentListing"):
    l=len(i.text.split())
    for j in range(0,l):
        a=i.text.split()[j]
        if a[0]=='(':
            k=j
            break
    pres.append(' '.join(i.text.split()[0:k]))          #To store only the names of respected former presidents of India

tf=[]
z=1
for i in soup.find_all('div',class_="presidentListing"):
    l=len(i.text.split())
    for j in range(0,l):
        a=i.text.split()[j]
        if a=='Office:':
            k=j
            break
    if z<=3:
        tf.append(' '.join(i.text.split()[k+1:l-1]))    #To store only the term of office of respected former presidents of India
        z=z+1
    else:
        tf.append(' '.join(i.text.split()[k+1:l])) 

pd.set_option("display.max_rows", None, "display.max_columns", None)
df=pd.DataFrame({'Name':pres, 'Term of Office':tf})
print("The list of respected former presidents of India")
df.set_index('Name', inplace=True)
df


# Q7# Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world :) Headline
# ii) Time
# iii) News Link
# 
# 

# In[12]:


from bs4 import BeautifulSoup as soup
import requests
import pandas as pd

page=requests.get("https://www.cnbc.com/world/?region=world")
page   #As the response is 200, we can proceed with this url

soup= BeautifulSoup(page7.content)

headline=[]                 #To store headlines
for i in soup.find_all('a',class_="LatestNews-headline"):
    headline.append(i.get('title'))
    
time=[]                    #To store time
for i in soup.find_all('time',class_="LatestNews-timestamp"):
    time.append(i.text)

url=[]                   #To store the urls
for i in soup.find_all('a',class_="LatestNews-headline"):
    url.append(i.get('href'))

l=len(headline)
s_no=[]
for j in range(1,l+1):
    s_no.append(j)

pd.set_option("display.max_rows", None, "display.max_columns", None)
df=pd.DataFrame({'Headline':headline, 'Time':time, 'News links':url}, index=s_no)
print("News details")
df


# In[8]:


#8) Write a python program to scrape the details of most downloaded articles from AI in last 90 days. 

#Scrape below mentioned details :
#i) Paper Title 
#ii) Authors
#iii) Published Date 
#iv) Paper URL 
page=requests.get("https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles")
page   #As the response is 200, we can proceed with this url

soup= BeautifulSoup(page8.content)

paper_title=[]           #To store the paper titles
for i in soup.find_all('h2',class_="sc-1qrq3sd-1 MKjKb sc-1nmom32-0 sc-1nmom32-1 hqhUYH ebTA-dR"):
    paper_title.append(i.text)

authors=[]               #To store the author names
for i in soup.find_all('span',class_="sc-1w3fpd7-0 pgLAT"):
    authors.append(i.text)
    
date=[]                  #To store the publication date
for i in soup.find_all('span',class_="sc-1thf9ly-2 bKddwo"):
    date.append(i.text)

url=[]                   #To store the urls
for i in soup.find_all('a',class_="sc-5smygv-0 nrDZj"):
    url.append(i.get('href'))

l=len(paper_title)
s_no=[]
for j in range(1,l+1):
    s_no.append(j)

pd.set_option("display.max_rows", None, "display.max_columns", None)
df=pd.DataFrame({'Paper Titles':paper_title, 'Authors':authors, 'Date of Publication':date, 'Paper Links':url}, index=s_no)
print("The details of most downloaded articles from AI in last 90 days")
df


# # 9) Write a python program to scrape mentioned details from dineout.co.in :
# i) Restaurant name
# ii) Cuisine
# iii) Location 
# iv) Ratings
# v) Image URL
# 

# In[16]:



page=requests.get("https://www.dineout.co.in/delhi-restaurants/buffet-special")
page   #As the response is 200, we can proceed with this url

soup= BeautifulSoup(page9.content)

r_name=[]           #To store the restaurant name
for i in soup.find_all('a',class_="restnt-name ellipsis"):
    r_name.append(i.text)

cuisine=[]           #To store the cuisine
for i in soup.find_all('span',class_="double-line-ellipsis"):
    cuisine.append(' '.join(i.text.split()[6:]))
cuisine

location=[]         #To store location
for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    location.append(i.text)
location

ratings=[]          #To store ratings
for i in soup.find_all('div',class_="restnt-rating rating-4"):
    ratings.append(i.text)

images=[]           #to store images
for i in soup.find_all('img',class_="no-img"):
    images.append(i['data-src'])
    
images

pd.set_option("display.max_rows", None, "display.max_columns", None)
df=pd.DataFrame({'Restaurant Name':r_name, 'Cuisine':cuisine, 'Location':location, 'Ratings':ratings, 'Image URL':images})
print("The details from dineout.co.in")
df.set_index('Restaurant Name', inplace=True)
df


# # 10 Write a python program to scrape the details of top publications from Google Scholar from 
# #https://scholar.google.com/citations?view_op=top_venues&hl=en
# i) Rank 
# ii) Publication
# iii) h5-index
#  iv) h5-median
# 

# In[6]:


page = requests.get('https://scholar.google.com/citations?view_op=top_venues&hl=en') # Send request to webserver to get the source code

soup = BeautifulSoup(page.content) # To Assign the page content to the variable soup
soup

publications = []
rank = []
h5index = []
h5median = []

# Assigning publication name to the variable
for title in soup.find_all('td', class_='gsc_mvt_t'):
    publications.append(title.text)
publications

# Assigning rank to the variable
for title in soup.find_all('td', class_='gsc_mvt_p'):
    rank.append(title.text)
rank

# Assigning h5_index to the variable
for title in soup.find_all('a', class_='gs_ibl gsc_mp_anchor'):
    h5index.append(title.text)
h5index

# Assigning h5_median to the variable
for title in soup.find_all('span', class_='gs_ibl gsc_mp_anchor'):
    h5median.append(title.text)
h5median

# Assigning data to the Dataframe
import pandas as pd
data = pd.DataFrame()
data['Rank'] = rank
data['Publication'] = publications
data['h5-index'] = h5index
data['h5-median'] = h5median
data


# In[55]:





# 6) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
# b) Top 10 ODI Batsmen along with the records of their team and rating.
# c) Top 10 ODI bowlers along with the records of their team and rating.
# 

# In[17]:


page6a=requests.get("https://www.icc-cricket.com/rankings/womens/team-rankings/odi")
page6a   #As the response is 200, we can proceed with this url

soup6a= BeautifulSoup(page6a.content)

a=soup6a.find('tr',class_="rankings-block__banner")    #Store the highest ranker
t=[]
m=[]
p=[]
r=[]
l=len(a.text.split())
for j in range(1,l):
    b=a.text.split()[j]
    if b[0]=='1' or b[0]=='2' or b[0]=='3' or b[0]=='4' or b[0]=='5' or b[0]=='6' or b[0]=='7' or b[0]=='8' or b[0]=='9':
        k=j
        break
t.append(' '.join(a.text.split()[1:k-1]))
m.append(''.join(a.text.split()[k]))
p.append(''.join(a.text.split()[k+1]))
r.append(''.join(a.text.split()[k+2]))

z=1                                #Counter to get only top 10
for i in soup6a.find_all('tr',class_="table-body"):
    if z<=9:
        l=len(i.text.split())
        for j in range(1,l):
            b=i.text.split()[j]
            if b[0]=='1' or b[0]=='2' or b[0]=='3' or b[0]=='4' or b[0]=='5' or b[0]=='6' or b[0]=='7' or b[0]=='8' or b[0]=='9':
                k=j
                break
        t.append(' '.join(i.text.split()[1:k-1]))
        m.append(''.join(i.text.split()[k]))
        p.append(''.join(i.text.split()[k+1]))
        r.append(''.join(i.text.split()[k+2]))
        z=z+1
              
s_no=[]
for j in range(1,11):
    s_no.append(j)

pd.set_option("display.max_rows", None, "display.max_columns", None)
df6a=pd.DataFrame({'Team':t, 'Matches':m, 'Points':p, 'Ratings':r}, index=s_no)
print("Top 10 ODI teams in women’s cricket along with the records for matches, points and rating")
df6a


# In[18]:


page6b=requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting")
page6b   #As the response is 200, we can proceed with this url

soup6b= BeautifulSoup(page6b.content)

a=soup6b.find('tr',class_="rankings-block__banner")    #Store the highest ranker
p=[]
t=[]
r=[]
l=len(a.text.split())
for j in range(2,l):
    b=a.text.split()[j]
    if b[0]=='9' or b[0]=='8' or b[0]=='7' or b[0]=='6' or b[0]=='5' or b[0]=='4' or b[0]=='1':
        k=j
        break
if a.text.split()[1]=='(0)':
    p.append(' '.join(a.text.split()[2:k-1]))
    t.append(''.join(a.text.split()[k-1]))
    r.append(''.join(a.text.split()[k]))
else:
    p.append(' '.join(a.text.split()[15:k-1]))
    t.append(''.join(a.text.split()[k-1]))
    r.append(''.join(a.text.split()[k]))

z=1                                #Counter to get only top 10
for i in soup6b.find_all('tr',class_="table-body"):
    if z<=9:
        l=len(i.text.split())
        for j in range(2,l):
            b=i.text.split()[j]
            if b[0]=='9' or b[0]=='8' or b[0]=='7' or b[0]=='6' or b[0]=='5' or b[0]=='4' or b[0]=='1':
                k=j
                break
        if i.text.split()[1]=='(0)':
            p.append(' '.join(i.text.split()[2:k-1]))
            t.append(''.join(i.text.split()[k-1]))
            r.append(''.join(i.text.split()[k]))
        else:
            p.append(' '.join(i.text.split()[15:k-1]))
            t.append(''.join(i.text.split()[k-1]))
            r.append(''.join(i.text.split()[k]))
        z=z+1
              
s_no=[]
for j in range(1,11):
    s_no.append(j)
    
pd.set_option("display.max_rows", None, "display.max_columns", None)
df6b=pd.DataFrame({'Batting Player':p, 'Team':t, 'Rating':r}, index=s_no)
print("Top 10 women’s ODI Batting players along with the records of their team and rating.")
df6b


# In[19]:


page6c=requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder")
page6c   #As the response is 200, we can proceed with this url

soup6c= BeautifulSoup(page6c.content)

a=soup6c.find('tr',class_="rankings-block__banner")    #Store the highest ranker
p=[]
t=[]
r=[]
l=len(a.text.split())
for j in range(2,l):
    b=a.text.split()[j]
    if b[0]=='1' or b[0]=='2' or b[0]=='3'  or b[0]=='4' or b[0]=='5' or b[0]=='6' or b[0]=='7' or b[0]=='8' or b[0]=='9':
        k=j
        break
if a.text.split()[1]=='(0)':
    p.append(' '.join(a.text.split()[2:k-1]))
    t.append(''.join(a.text.split()[k-1]))
    r.append(''.join(a.text.split()[k]))
else:
    p.append(' '.join(a.text.split()[15:k-1]))
    t.append(''.join(a.text.split()[k-1]))
    r.append(''.join(a.text.split()[k]))

z=1                                #Counter to get only top 10
for i in soup6c.find_all('tr',class_="table-body"):
    if z<=9:
        l=len(i.text.split())
        for j in range(2,l):
            b=i.text.split()[j]
            if b[0]=='1' or b[0]=='2' or b[0]=='3'  or b[0]=='4' or b[0]=='5' or b[0]=='6' or b[0]=='7' or b[0]=='8' or b[0]=='9':
                k=j
                break
        if i.text.split()[1]=='(0)':
            p.append(' '.join(i.text.split()[2:k-1]))
            t.append(''.join(i.text.split()[k-1]))
            r.append(''.join(i.text.split()[k]))
        else:
            p.append(' '.join(i.text.split()[15:k-1]))
            t.append(''.join(i.text.split()[k-1]))
            r.append(''.join(i.text.split()[k]))
        z=z+1
              
s_no=[]
for j in range(1,11):
    s_no.append(j)

pd.set_option("display.max_rows", None, "display.max_columns", None)
df6c=pd.DataFrame({'All Rounder':p, 'Team':t, 'Rating':r}, index=s_no)
print("Top 10 women’s ODI all-rounder along with the records of their team and rating.")
df6c


# In[ ]:


5) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
b) Top 10 ODI Batsmen along with the records of their team and rating.
c) Top 10 ODI bowlers along with the records of their team and rating.


# In[20]:


# 5a. Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape: a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating. 

page5a=requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")
page5a   #As the response is 200, we can proceed with this url

soup5a= BeautifulSoup(page5a.content)

a=soup5a.find('tr',class_="rankings-block__banner")    #Store the highest ranker
t=[]
m=[]
p=[]
r=[]
l=len(a.text.split())
for j in range(1,l):
    b=a.text.split()[j]
    if b[0]=='1' or b[0]=='2' or b[0]=='3' or b[0]=='4' or b[0]=='5':
        k=j
        break
t.append(' '.join(a.text.split()[1:k-1]))
m.append(''.join(a.text.split()[k]))
p.append(''.join(a.text.split()[k+1]))
r.append(''.join(a.text.split()[k+2]))

z=1                                #Counter to get only top 10
for i in soup5a.find_all('tr',class_="table-body"):
    if z<=9:
        l=len(i.text.split())
        for j in range(1,l):
            b=i.text.split()[j]
            if b[0]=='1' or b[0]=='2' or b[0]=='3' or b[0]=='4' or b[0]=='5':
                k=j
                break
        t.append(' '.join(i.text.split()[1:k-1]))
        m.append(''.join(i.text.split()[k]))
        p.append(''.join(i.text.split()[k+1]))
        r.append(''.join(i.text.split()[k+2]))
        z=z+1
              
s_no=[]
for j in range(1,11):
    s_no.append(j)

pd.set_option("display.max_rows", None, "display.max_columns", None)
df5a=pd.DataFrame({'Team':t, 'Matches':m, 'Points':p, 'Ratings':r}, index=s_no)
print("Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.")
df5a


# In[21]:


page5b=requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting")
page5b   #As the response is 200, we can proceed with this url

soup5b= BeautifulSoup(page5b.content)

a=soup5b.find('tr',class_="rankings-block__banner")    #Store the highest ranker
p=[]
t=[]
r=[]
l=len(a.text.split())
for j in range(2,l):
    b=a.text.split()[j]
    if b[0]=='9' or b[0]=='8' or b[0]=='7' or b[0]=='1':
        k=j
        break
p.append(' '.join(a.text.split()[2:k-1]))
t.append(''.join(a.text.split()[k-1]))
r.append(''.join(a.text.split()[k]))

z=1                                #Counter to get only top 10
for i in soup5b.find_all('tr',class_="table-body"):
    if z<=9:
        l=len(i.text.split())
        for j in range(2,l):
            b=i.text.split()[j]
            if b[0]=='9' or b[0]=='8' or b[0]=='7' or b[0]=='1':
                k=j
                break
        if i.text.split()[1]=='(0)':
            p.append(' '.join(i.text.split()[2:k-1]))
            t.append(''.join(i.text.split()[k-1]))
            r.append(''.join(i.text.split()[k]))
        else:
            p.append(' '.join(i.text.split()[15:k-1]))
            t.append(''.join(i.text.split()[k-1]))
            r.append(''.join(i.text.split()[k]))
        z=z+1
              
s_no=[]
for j in range(1,11):
    s_no.append(j)

pd.set_option("display.max_rows", None, "display.max_columns", None)
df5b=pd.DataFrame({'Batsmen':p, 'Team':t, 'Rating':r}, index=s_no)
print("Top 10 ODI Batsmen along with the records of their team and rating.")
df5b


# In[22]:


page5c=requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling")
page5c   #As the response is 200, we can proceed with this url

soup5c= BeautifulSoup(page5c.content)

a=soup5c.find('tr',class_="rankings-block__banner")    #Store the highest ranker
p=[]
t=[]
r=[]
l=len(a.text.split())
for j in range(2,l):
    b=a.text.split()[j]
    if b[0]=='9' or b[0]=='8' or b[0]=='7' or b[0]=='6' or b[0]=='1':
        k=j
        break
p.append(' '.join(a.text.split()[2:k-1]))
t.append(''.join(a.text.split()[k-1]))
r.append(''.join(a.text.split()[k]))

z=1                                #Counter to get only top 10
for i in soup5c.find_all('tr',class_="table-body"):
    if z<=9:
        l=len(i.text.split())
        for j in range(2,l):
            b=i.text.split()[j]
            if b[0]=='9' or b[0]=='8' or b[0]=='7' or b[0]=='6' or b[0]=='1':
                k=j
                break
        if i.text.split()[1]=='(0)':
            p.append(' '.join(i.text.split()[2:k-1]))
            t.append(''.join(i.text.split()[k-1]))
            r.append(''.join(i.text.split()[k]))
        else:
            p.append(' '.join(i.text.split()[15:k-1]))
            t.append(''.join(i.text.split()[k-1]))
            r.append(''.join(i.text.split()[k]))
        z=z+1
              
s_no=[]
for j in range(1,11):
    s_no.append(j)

pd.set_option("display.max_rows", None, "display.max_columns", None)
df5c=pd.DataFrame({'Bowler':p, 'Team':t, 'Rating':r}, index=s_no)
print("Top 10 ODI Bowlers along with the records of their team and rating.")
df5c


# In[ ]:




