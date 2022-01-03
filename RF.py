x=df.drop(['0.000000000000000000e+00.88'], axis=1)
y=df['0.000000000000000000e+00.88']

x_train,x_test,y_train,y_test= train_test_split(x,y,random_state=17,test_size=0.3)

# model
clf = RandomForestClassifier(max_depth=10, random_state=0)

clf.fit(x_train,y_train)

# scores
scores_RF = cross_val_score(clf, x, y, cv=10)

print('----------------cross validation---------------------')
print(scores_RF) #cross validation
print('------------------avg-------------------')
print(scores_RF.mean()) #avg
print('------------------classification_report-------------------')

y_pred = clf.predict(x_test)

print(classification_report(y_pred, y_test))

plot_confusion_matrix(clf, x_test, y_test)
plt.title("Random forrest")
plt.show()
