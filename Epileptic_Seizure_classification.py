#!/usr/bin/env python
# coding: utf-8

# In[13]:


import os
import pandas as pd
import glob
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import TimeSeriesSplit
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split ,cross_val_score
from sklearn.metrics import classification_report, plot_confusion_matrix, confusion_matrix
import matplotlib.pyplot as plt
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


# In[14]:



df = pd.read_csv("Epileptic Seizure Recognition.csv")
df.head()


# In[ ]:





# In[15]:


df.isnull().sum()


# In[ ]:





# In[ ]:





# In[16]:


#label_encoder = preprocessing.LabelEncoder()
#df['Direction']= label_encoder.fit_transform(df['Direction'])



# In[ ]:





# In[ ]:





# In[17]:


columns = list(df.columns.values[1:-1])

min_max = preprocessing.MinMaxScaler()
df[columns] = min_max.fit_transform(df[columns])


# In[18]:


df['y'] = df['y'].replace([2,3,4,5],0)
df


# In[20]:


x=df.drop(['y','Unnamed'], axis=1)
y=df['y']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42 ,stratify=y)
#x_train, x_test, y_train, y_test = StratifiedShuffleSplit(n_splits=5, test_size=0.2, random_state=42)
model=KNeighborsClassifier(n_neighbors=3)

model.fit(x_train,y_train)
y_pred = model.predict(x_test)
plot_confusion_matrix(model, x_test, y_test)
print(classification_report(y_pred, y_test))
plt.title("KNN euclidean")
plt.show()


# In[ ]:





# In[24]:


model1=KNeighborsClassifier(n_neighbors=1)

model1.fit(x_train,y_train)
y_pred1 = model1.predict(x_test)
plot_confusion_matrix(model1, x_test, y_test)
print(classification_report(y_pred1, y_test))
plt.title("KNN euclidean")
plt.show()


# In[21]:


dt = DecisionTreeClassifier(random_state=42)
dt = dt.fit(x_train, y_train)
y_pred = dt.predict(x_test)
print(classification_report(y_pred, y_test))
plot_confusion_matrix(dt, x_test, y_test)
plt.title("Decison Tree")
plt.show()


# In[26]:


rf = RandomForestClassifier(max_depth=10, random_state=42)

rf.fit(x_train,y_train)
y_pred2 = rf.predict(x_test)

print(classification_report(y_pred2, y_test))

plot_confusion_matrix(rf, x_test, y_test)
plt.title("Random forest")
plt.show()


# In[22]:


from tensorflow.keras import Sequential,utils
from tensorflow.keras.layers import Flatten, Dense, Conv1D, MaxPool1D, Dropout
import seaborn as sns


# In[23]:


print(df.shape)

x=df.drop(['y','Unnamed'], axis=1)
y=df['y']

x_train,x_test,y_train,y_test= train_test_split(x,y,random_state=17,test_size=0.3)

CNN_Model = Sequential()

CNN_Model.add(Conv1D(filters=32, kernel_size=(3,), padding='same', activation='relu', input_shape = (x_train.shape[1],1)))
CNN_Model.add(Conv1D(filters=64, kernel_size=(3,), padding='same', activation='relu')) 
CNN_Model.add(Conv1D(filters=128, kernel_size=(5,), padding='same', activation='relu'))    

CNN_Model.add(MaxPool1D(pool_size=(3,), strides=2, padding='same'))
CNN_Model.add(Dropout(0.5))

CNN_Model.add(Flatten())

CNN_Model.add(Dense(units = 512, activation='relu'))
CNN_Model.add(Dense(units = 1024, activation='relu'))
CNN_Model.add(Dense(units = 6, activation='softmax'))

CNN_Model.compile(optimizer='adam', loss = 'sparse_categorical_crossentropy', metrics=['accuracy'])

Epochs = CNN_Model.fit(x_train, y_train, epochs = 10)


# In[ ]:





# In[ ]:




