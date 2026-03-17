from sklearn import tree

#[height,weight]

x = [[181,80],[177,70],[160,60],[154,54],[166,65],[190,90],[175,64],[177,70],[159,55]]

y = ["male","female","female","female","male","male","male","female","female"]

clf = tree.DecisionTreeClassifier()

clf = clf.fit(x,y)

prediction = clf.predict([[160,150]])

print(prediction)