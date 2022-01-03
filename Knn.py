# df= pd.read_csv("/content/drive/MyDrive/mitbih_train.csv")

print(df.shape)

x=df.drop(['0.000000000000000000e+00.88'], axis=1)
y=df['0.000000000000000000e+00.88']

x_train,x_test,y_train,y_test= train_test_split(x,y,random_state=17,test_size=0.3)

model=KNeighborsClassifier(n_neighbors=5)

model.fit(x_train,y_train)


scores = cross_val_score(model, x, y, cv=10)

print('----------------cross validation---------------------')
print(scores) #cross validation
print('------------------avg-------------------')
print(scores.mean()) #avg
print('------------------classification_report-------------------')

y_pred = model.predict(x_test)

print(classification_report(y_pred, y_test))

plot_confusion_matrix(model, x_test, y_test)
plt.title("KNN euclidean")
plt.show()
