# -*- coding: utf-8 -*-
"""covid-19.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VleG5nTkuqPNMwXYGrrzI2PcP2uCccuB
"""

from google.colab import drive
drive.mount('/gdrive')

# importing required modules 
from zipfile import ZipFile 

# specifying the zip file address 
file_name = "/gdrive/My Drive/metadata.csv.zip"

# opening the zip file in READ mode 
with ZipFile(file_name, 'r') as zip:

	# extracting all the files 
	print('Extracting all the files now...') 
	zip.extractall('/content') 
	print('Done!')

import csv
metadata = '/content/metadata.csv'
with open(metadata, 'r') as csvfile:
  readdata = csv.reader(csvfile, delimiter=',', quotechar='"' )
  data = list(readdata)
print(len(data))
for i in range(10):
  print(data[i])

# Setup
!pip install -q wordcloud
import wordcloud
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger') 
import matplotlib.pyplot as plt
import io
import unicodedata
import numpy as np
import string

checkdata = input('enter the data that you want to search.')
# Get stopwords
stopwords = nltk.corpus.stopwords.words('english')
# Get punctuation
y = str(string.punctuation)
punctuation = []
for i in range(len(y)):
  punctuation.append(y[i])

# Tokenize by sentence, then by lowercase word
tokens = [word.lower() for sent in nltk.sent_tokenize(checkdata) for word in nltk.word_tokenize(sent)]
print(len(tokens))
tokenset = set(tokens)
print(len(tokenset))
tokenset = tokenset.difference(set(stopwords+punctuation))
print(tokenset)
N =print(len(tokenset))
# number of terms in the check document N
N = len(tokenset)

import numpy as np

#to operate index operation we need to convert the set into list
tokenlist = list(tokenset)

#only checking how is data and find the index of abstrack
print(data[1])
print(len(data[1][8]))

#create a numpy  array of shape(no. of tokens to check, no. of data in dataset)
#a[i][j] contain no. of times ith token comes in abstract of jth document divided by (length of abstract/length of token)
#a[i][j]basically gives idea about how frequently the ith token occurs in jth document.
a = np.zeros((N,len(data)), dtype=np.float64  )
for i in range(1,len(data)):
  for j in range(len(tokenlist)):
    N1 = len(data[i][8])/len(tokenlist[j])
    if N1 > 5:
      N2 = (data[i][8].lower().count(tokenlist[j]))/N1
    else:
      N2 = 0
    a[j][i] = N2


#checking the a matrix
print(a[1][:])

#if any word occur in every document then this word should given less priority in finding answer.
#greater priority should given to unique words that occur in few documents frequently.
#to do this we create new numpy array b and provide the value of b[i][j] = 1 if a[i][j]>1 (means count in not zero)
b = np.zeros_like(a)
for i in range(1,len(data)):
  for j in range(len(tokenlist)):
    if a[j][i] > 0:
      b[j][i] = 1
#c gives sum of each row , it gives the count of document in which the word is present
c = np.sum( b, axis = 1 ) 

#checking the matrix c and its shape
print( c )
print(c.shape)

# e matrix will have the weightage of the words to find the answer
d = np.divide(len(data),c)
d.reshape((1,N))
print(len(d))
for i in range(len(d)):
  if(np.isinf(d[i])):
    d[i]=1
e = np.log(d)
print(e)
print(e.shape)

# f matrix have the possibility of answer in the document 
f = np.dot(e,a)
print(f.shape)
print(f)

import matplotlib.pyplot as plt 

# x axis values 
x = list(range(len(data)))
y = f

#plotting the points 
plt.plot(x,y, color='yellow', linestyle='dashed', linewidth = 0.3, 
         marker='o', markerfacecolor='blue', markersize=12)  

# naming the x axis 
plt.xlabel('index of data') 
# naming the y axis 
plt.ylabel('posibility of answer') 

# giving a title to my graph 
plt.title('covid-19') 

# function to show the plot 
plt.show()

#abstracting of data 
# you can change the value of filtr from above graph such that sufficient amount of data get filtered here i choose filter is 0.6 so all the data below 0.6 get filtered.
count = 0
filtr = 0.6
for i in range(len(data)):
  if f[i]>filtr:
    print(data[i][8])
    print(f[i])
    count = count+1
print(count)