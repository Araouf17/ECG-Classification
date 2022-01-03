x=df.drop(['0.000000000000000000e+00.88'], axis=1)
y=df['0.000000000000000000e+00.88']
x_train,x_test,y_train,y_test =train_test_split(x,y,random_state=42,test_size=0.3)
clf_xgb = xgb.XGBClassifier(objective='binary:logistic', seed=42)
clf_xgb.fit(x_train,y_train)
clf_xgb.fit(x_train, y_train, early_stopping_rounds=10, eval_metric='aucpr', eval_set=[(x_test, y_test)])

# scores
scores_RF = cross_val_score(clf_xgb, x, y, cv=10)

print('----------------cross validation---------------------')
print(scores_RF) #cross validation
print('------------------avg-------------------')
# print(scores_RF.mean()) #avg
# print('------------------classification_report-------------------')

y_pred = clf_xgb.predict(x_test)

print(classification_report(y_pred, y_test))

plot_confusion_matrix(clf_xgb, x_test, y_test)
plt.title("Xgboost")
plt.show()
