import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from textblob import TextBlob
#Loading Dataset 
CommentDataset=pd.read_csv('GBcomments.csv' , error_bad_lines=False) #You Will Face A ParserError so You Have To define an error_bad_lines To False
#Have A look At A preview Of Your Dataset And Its Features 
print(CommentDataset.head(10))
print(CommentDataset.describe())
print(CommentDataset.info())
#--------------------- A VERY IMPORTANT SIDE NOTE-------------------------
#WHEN YOU BUILD SENTIMeNT ANALYSIS MODEL YOU HAVE TO INSTALL 'textblob' Library BEFORE YOU PREFORM SENTIMANT ANALYSIS
#After That i preform some quality check to find if there is a missing Data Or Not
print(CommentDataset.isnull().sum())
#Because We Have A Large And big Dataset With respect to the number of missing Data points its Okay to drop these null values
CommentDataset.dropna(inplace=True )
# Check again that this line of code go well
print(CommentDataset.isnull().sum())
#ALL GOOD LETS CONTAINUE
#Lets Do Sentiment Analysis for eacj=h and every Row in Your Dataset
#So you Have To Build For Loop To Loop Through All Rows In Your Dataset
Polarity=[] # AN EMPTY LIST TO APPEND EACH SENTIMENT POLARITY ON IT 
for Item in CommentDataset['comment_text']:
    Polarity.append(TextBlob(Item).sentiment.polarity)
#After All I have to add Polarity as a new column to dataset 
CommentDataset['Polarity']=Polarity
#After That we will preform EDA On sentiment Analysis Results AND specialy for positive Sentiments
Positive_Comments=CommentDataset[CommentDataset['Polarity'] ==1] # coping a Dataframe depend on boolean conditional indexing technique
#You Have To install wordcloud package to visualize Your textual Data ,Significant textual data points can be highlighted using a word cloud. 
from wordcloud import WordCloud , STOPWORDS
stopwords =set(STOPWORDS)
total_comments=' '.join(Positive_Comments['comment_text'])
wordcloud=WordCloud(width=1000 , height=500 , stopwords=stopwords ).generate(total_comments)
plt.figure(figsize=(15,5))
plt.imshow(wordcloud)
plt.axis(False)
#____________________
#Do the same previous EDA On sentiment Analysis Results but for negative Sentiments
Negative_Comments=CommentDataset[CommentDataset['Polarity'] ==-1] #some thing like coping a Dataframe
from wordcloud import WordCloud , STOPWORDS
stopwords =set(STOPWORDS)
total_comments=' '.join(Negative_Comments['comment_text'])
wordcloud=WordCloud(width=1000 , height=500 , stopwords=stopwords ).generate(total_comments)
plt.figure(figsize=(15,5))
plt.imshow(wordcloud)
plt.axis(False)
VideoDataset=pd.read_csv("GBvideos.csv" , error_bad_lines=False)
print(VideoDataset.head(10))
Tags_complete=' '.join(VideoDataset['tags'])
#there is some Data noise will remove it by re module
import re
tags=re.sub('[^a-zA-Z]' ,' ' ,Tags_complete)
tags=re.sub(' +' , ' ' ,tags)
from wordcloud import WordCloud , STOPWORDS
stopwords=set(STOPWORDS)
wordcloud=WordCloud(width=1000 , height=500 ,stopwords=stopwords).generate(tags)
plt.figure(figsize=(15,5))
plt.imshow(wordcloud)
plt.axis(False)
sns.regplot(data=VideoDataset ,x='views',y='likes' )
plt.title('regression plot for views and likes'.title())
plt.show()
Corr=VideoDataset[['views' , 'likes' , 'dislikes']].corr()
sns.heatmap(Corr , annot=True)
plt.show()
import emoji
string=''
#Do some preview on how the for  loop execuate along all comments
comment=CommentDataset['comment_text'][11]
lis=[c for c in comment if c in emoji.UNICODE_EMOJI]
for i in lis:
    string=string+i
string=''
lis=[]
for item in CommentDataset['comment_text']:
    for c in item:
       if c in emoji.UNICODE_EMOJI:
           lis.append(c)
Result={}
for i in set(string):
    Result[i]=string.count(i)

print(Result.items())

       
    
    
   
        




