x=df.drop(['Direction'], axis=1)
y=df['Direction']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42 ,stratify=y)
#x_train, x_test, y_train, y_test = StratifiedShuffleSplit(n_splits=5, test_size=0.2, random_state=42)
model=KNeighborsClassifier(n_neighbors=3)

model.fit(x_train,y_train)
y_pred = model.predict(x_test)
plot_confusion_matrix(model, x_test, y_test)
print(classification_report(y_pred, y_test))
plt.title("KNN euclidean")
plt.show()


model1=KNeighborsClassifier(n_neighbors=1)

model1.fit(x_train,y_train)
y_pred1 = model1.predict(x_test)
plot_confusion_matrix(model1, x_test, y_test)
print(classification_report(y_pred1, y_test))
plt.title("KNN euclidean")
plt.show()
